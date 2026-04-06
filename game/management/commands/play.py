from django.core.management.base import BaseCommand
from game.models import Game
from game.logic import TicTacToeLogic
from django.utils import timezone


class Command(BaseCommand):
    help = "Tic-Tac-Toe"

    def handle(self, *args, **options):
        game = Game()

        self.stdout.write("\n·····························")
        self.stdout.write("\tTic-Tac-Toe\n")
        self.stdout.write("·····························")

        try:
            while not game.is_finished:
                self.graph_board(game.board)

                move_input = input(f"\nTurno de {game.turn}, elige posición (0 - 8): ")

                if move_input == "q":
                    self.abort_game(game)
                    return

                if not move_input.isdigit():
                    self.stdout.write(self.style.ERROR("\nIntroduce un número"))
                    continue

                success, message = TicTacToeLogic.make_move(game, int(move_input))

                if not success:
                    self.stdout.write(self.style.NOTICE(message))

            self.graph_board(game.board)
            self.result(game)

        except KeyboardInterrupt:
            self.abort_game(game)

    def graph_board(self, b):
        self.stdout.write("\n")

        for i in range(0, 9, 3):
            self.stdout.write(f" {b[i]} | {b[i+1]} | {b[i+2]} ")

            if i < 6:
                self.stdout.write("-----------")

        self.stdout.write("\n")

    def result(self, game):
        if game.winner == "Draw":
            self.stdout.write(self.style.WARNING("Empate!"))
        else:
            self.stdout.write(self.style.SUCCESS(f"Gana {game.winner}!"))

    def abort_game(self, game):
        self.stdout.write(self.style.WARNING("\nPartida cancelada"))

        if game.id:
            game.winner = "Abandoned"
            game.is_finished = True
            game.finished_at = timezone.now()
            game.save()
