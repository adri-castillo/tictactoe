from django.core.management.base import BaseCommand
from game.models import Game
from game.logic import TicTacToeLogic


class Command(BaseCommand):
    help = "Tic-Tac-Toe"

    def handle(self, *args, **options):
        game = Game.objects.create()

        self.stdout.write("\n·····························")
        self.stdout.write("\tTic-Tac-Toe\n")
        self.stdout.write("·····························")

        try:
            while not game.is_finished:
                self.graph_board(game.board)

                # Input movimiento
                move_input = input(f"\nTurno de {game.turn}, elige posición (0 - 8): ")

                # Salir del juego
                if move_input == "q":
                    self.stdout.write(self.style.WARNING("\nPartida cancelada"))
                    return

                # Validar solo numeros
                if not move_input.isdigit():
                    self.stdout.write(self.style.ERROR("\nIntroduce un número"))
                    continue

                # Procesar movimiento
                success, message = TicTacToeLogic.make_move(game, int(move_input))

                if success:
                    game.refresh_from_db()
                else:
                    self.stdout.write(self.style.NOTICE(message))

            # Fin del juego
            self.graph_board(game.board)
            self.result(game)

        except KeyboardInterrupt:
            self.stdout.write(self.style.WARNING("\nPartida cancelada"))

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
