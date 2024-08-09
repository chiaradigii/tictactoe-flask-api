import unittest
from app import create_app, db
from app.models import Game
import json

class TicTacToeTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app.config['TESTING'] = True
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.client = self.app.test_client()

        with self.app.app_context():
            db.create_all()

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def test_create_game(self):
        response = self.client.post('/create')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertIn('gameId', data)

    def test_make_move(self):
        response = self.client.post('/create')
        game_id = json.loads(response.data)['gameId']

        move_data = {
            "gameId": game_id,
            "playerId": "X",
            "square": {"x": 0, "y": 0}
        }
        response = self.client.post('/move', json=move_data)
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['status'], "ongoing")

    def test_game_status(self):
        response = self.client.post('/create')
        game_id = json.loads(response.data)['gameId']

        response = self.client.get(f'/status?gameId={game_id}')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['currentPlayer'], "X")
        self.assertEqual(data['status'], "ongoing")

if __name__ == '__main__':
    unittest.main()
