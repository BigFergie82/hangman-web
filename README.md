# Letter by letter - Hangman Web

A Python/Flask Hangman application for CSE 4095. The browser only displays
server state; it never receives the answer until the game ends.

Live app: https://malcolm-hangman-web.onrender.com

Repository: https://github.com/BigFergie82/hangman-web

## Run locally

Requires Python 3.11 or newer.

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python server.py
```

Open http://127.0.0.1:5000. On macOS/Linux activate with
`source .venv/bin/activate` instead.

## Test

From the project root:

```text
python -m unittest discover -s tests -v
```

The 16 tests cover the engine, word-list validation, difficulties, API
validation, independent games, duplicates, secrecy, wins, losses and restart.

## Architecture

- `game.py`: independent Hangman rules, six misses and safe serialization.
- `word_manager.py` and `words/`: curated server-side difficulty lists.
- `server.py`: Flask app factory, opaque game IDs, validation and game storage.
- `templates/index.html`, `static/`: responsive UI, SVG drawing and fetch client.
- `Specification.md`: unchanged original reference; `ASSIGNMENT.md`: reduced scope.
- `TODO.md`: adapted, verified phase checklist.

## REST API

| Method | Path | JSON body | Result |
| --- | --- | --- | --- |
| POST | `/api/games` | `{"difficulty":"easy"}` | 201, new state and game_id |
| GET | `/api/games/<game_id>` | None | 200, current state |
| POST | `/api/games/<game_id>/guess` | `{"letter":"e"}` | 200, updated state |
| GET | `/health` | None | 200, health status |

Difficulty is easy, medium or hard. Invalid JSON or fields return 400;
unknown IDs return 404; duplicate/post-game guesses return 409; non-JSON
requests return 415. Errors are JSON. The answer appears only in a terminal
state's `word` field. Uppercase guesses are normalized. Extra input fields
are rejected. Active API responses use `Cache-Control: no-store`.

## Render deployment

Create a **Python Web Service** from this repository's main branch, using
the **Free** plan and these commands:

- Build: `pip install -r requirements.txt && python -m unittest discover -s tests -v`
- Start: `gunicorn --bind 0.0.0.0:$PORT --workers 1 --threads 4 server:app`
- Optional HTTP health path: `/health`.
- Python version: `3.13.7` (environment variable `PYTHON_VERSION`).

This deployment was created using a public Git repository URL. If pushing a
commit does not produce a new deployment, use Manual Deploy > Deploy latest
commit in Render. Confirm the live deployment's commit before grading.

Use exactly one worker: game state is held in memory. A lock protects
updates across threads. A restart, redeploy or free-service spin-down
clears games; users can start a new one. Idle games are removed during new
game creation after 24 hours. Storage is capped at 10,000 games.
There is no account, database, leaderboard, terminal client or bot.
Free hosting can take about one minute to wake after inactivity.

## Demonstration and submission

Follow `DEMONSTRATION.md` for the required 2-3 minute recording. Submit the
repository URL, verified public app URL, PDF report and screen recording
through HuskyCT. Keep the service available during grading.
