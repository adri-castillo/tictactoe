class TicTacToeLogic:
    def check_winner(board):
        winning_combinations = [
            (0, 1, 2),
            (3, 4, 5),
            (6, 7, 8),
            (0, 3, 6),
            (1, 4, 7),
            (2, 5, 8),
            (0, 4, 8),
            (2, 4, 6),
        ]

        for x, y, z in winning_combinations:
            if board[x] == board[y] == board[z] != " ":
                return board[x]
            
        if " " not in board:
            return "Draw"  

        return None

    def make_move(game, position):
        if not (0 <= position <= 8) or game.board[position] != " ":
            return False, "\nMovimiento no válido"

        # Actualizar tablero
        board_list = list(game.board)
        board_list[position] = game.turn
        game.board = "".join(board_list)

        winner = TicTacToeLogic.check_winner(game.board)

        if winner:
            game.winner = winner
            game.is_finished = True
        else:
            game.turn = "O" if game.turn == "X" else "X"

        game.save()

        return True, "\nMovimiento realizado!"
