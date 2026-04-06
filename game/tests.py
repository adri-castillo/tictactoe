from django.test import TestCase
from game.models import Game
from game.logic import TicTacToeLogic


class TicTacToeTest(TestCase):

    def setUp(self):
        self.game = Game.objects.create()

    def test_initial_board_empty(self):
        self.assertEqual(self.game.board, " " * 9)
        self.assertEqual(self.game.is_finished, False)

    def test_valid_movement(self):
        success = TicTacToeLogic.make_move(self.game, 0)

        self.assertTrue(success)
        self.assertEqual(self.game.board[0], "X")
        self.assertEqual(self.game.turn, "O")

    def test_occupied_box(self):
        TicTacToeLogic.make_move(self.game, 4)

        success, message = TicTacToeLogic.make_move(self.game, 4)

        self.assertFalse(success)
        self.assertIn("\nMovimiento no válido", message)

    def test_check_winner_scenarios(self):
        cases = [
            ("OOO      ", "O"),
            ("X  X  X  ", "X"),
            ("X   X   X", "X"),
            ("XOXOOXXXO", "Draw"),
        ]
        for board, result in cases:
            self.assertEqual(TicTacToeLogic.check_winner(board), result)
