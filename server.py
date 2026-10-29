"""Server-authoritative Hangman API; deploy with a single Gunicorn worker."""
import secrets
import time
from threading import RLock
from flask import Flask, jsonify, render_template, request
from werkzeug.exceptions import HTTPException
from game import HangmanGame, GuessError
from word_manager import WordManager


def create_app(word_manager=None):
    app = Flask(__name__)
    app.config['MAX_CONTENT_LENGTH'] = 4096
    words = word_manager or WordManager()
    games = {}
    lock = RLock()
    app.extensions['games'] = games

    def body(required):
        if not request.is_json:
            return None, (jsonify(error='Send application/json.'), 415)
        data = request.get_json()
        if not isinstance(data, dict) or set(data) != {required}:
            return None, (jsonify(error=f'Provide exactly one field: {required}.'), 400)
        return data, None

    def state(game_id, game):
        return dict(game.public_state(), game_id=game_id)

    @app.after_request
    def headers(response):
        response.headers['X-Content-Type-Options'] = 'nosniff'
        if request.path.startswith('/api/'):
            response.headers['Cache-Control'] = 'no-store'
        return response

    @app.errorhandler(HTTPException)
    def http_error(error):
        return jsonify(error=error.description), error.code

    @app.get('/')
    def home():
        return render_template('index.html')

    @app.get('/health')
    def health():
        return jsonify(status='ok')

    @app.post('/api/games')
    def create_game():
        data, error = body('difficulty')
        if error:
            return error
        try:
            game = HangmanGame(words.random_word(data['difficulty']))
        except ValueError as exc:
            return jsonify(error=str(exc)), 400
        with lock:
            now = time.monotonic()
            for key in list(games):
                if now - games[key][1] > 86400:
                    del games[key]
            if len(games) >= 10000:
                return jsonify(error='Game capacity reached. Please try later.'), 503
            game_id = secrets.token_hex(16)
            games[game_id] = (game, now)
        return jsonify(state(game_id, game)), 201

    @app.get('/api/games/<game_id>')
    @app.post('/api/games/<game_id>/guess')
    def game_request(game_id):
        with lock:
            entry = games.get(game_id)
            if entry is None:
                return jsonify(error='Game not found. Start a new game.'), 404
            game, _ = entry
            if request.method == 'POST':
                data, error = body('letter')
                if error:
                    return error
                try:
                    game.guess(data['letter'])
                except GuessError as exc:
                    return jsonify(error=str(exc), code=exc.code), (400 if exc.code == 'invalid_letter' else 409)
            games[game_id] = (game, time.monotonic())
            return jsonify(state(game_id, game))

    return app


app = create_app()

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
