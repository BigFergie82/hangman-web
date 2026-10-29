import unittest
from server import create_app


class Words:
    def random_word(self, difficulty):
        if difficulty not in ('easy', 'medium', 'hard'):
            raise ValueError('Invalid difficulty')
        return 'cat'


class ApiTests(unittest.TestCase):
    def setUp(self):
        self.client = create_app(Words()).test_client()

    def new(self, difficulty='easy'):
        response = self.client.post('/api/games', json={'difficulty': difficulty})
        self.assertEqual(response.status_code, 201)
        self.assertNotIn('word', response.json)
        return '/api/games/' + response.json['game_id']

    def test_difficulties_and_isolation(self):
        for difficulty in ('easy', 'medium', 'hard'):
            first, second = self.new(difficulty), self.new(difficulty)
            self.assertNotEqual(first, second)
            self.client.post(first + '/guess', json={'letter': 'c'})
            self.assertEqual(self.client.get(second).json['guessed_letters'], [])

    def test_win_and_restart(self):
        path = self.new()
        for letter in 'cat':
            response = self.client.post(path + '/guess', json={'letter': letter})
        self.assertEqual(response.json['status'], 'won')
        self.assertEqual(response.json['word'], 'cat')
        self.assertEqual(self.client.post(path+'/guess', json={'letter':'x'}).status_code, 409)
        self.new()

    def test_loss(self):
        path = self.new()
        for letter in 'bdefgh':
            response = self.client.post(path+'/guess', json={'letter':letter})
        self.assertEqual(response.json['status'], 'lost')
        self.assertEqual(response.json['remaining_guesses'], 0)

    def test_invalid_requests_and_secrecy(self):
        path = self.new()
        for value in ('', 'ab', 1, None, 'é'):
            self.assertEqual(self.client.post(path+'/guess', json={'letter':value}).status_code, 400)
        self.assertEqual(self.client.post(path+'/guess', json={'letter':'c'}).status_code, 200)
        self.assertEqual(self.client.post(path+'/guess', json={'letter':'C'}).status_code, 409)
        self.assertNotIn('word', self.client.get(path).json)
        self.assertEqual(self.client.get(path).json['remaining_guesses'], 6)
        self.assertEqual(self.client.post('/api/games', json={'difficulty':'bad'}).status_code, 400)
        self.assertEqual(self.client.post('/api/games', json=[]).status_code, 400)
        self.assertEqual(self.client.post('/api/games', data='{}').status_code, 415)
        self.assertEqual(self.client.post('/api/games', data='{', content_type='application/json').status_code, 400)
        self.assertEqual(self.client.get('/api/games/missing').status_code, 404)
        self.assertEqual(self.client.post(path+'/guess', json={'letter':'a','word':'cat'}).status_code, 400)

    def test_home_and_health(self):
        self.assertEqual(self.client.get('/').status_code, 200)
        self.assertEqual(self.client.get('/health').json['status'], 'ok')


if __name__ == '__main__':
    unittest.main()
