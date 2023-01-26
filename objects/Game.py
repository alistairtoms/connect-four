from exceptions import ColumnFullError
from objects.Board import Board
from players.BasePlayer import BasePlayer


class Game:
    """A class to hold all the game information like board state and turn status."""

    def __init__(self, player1: BasePlayer, player2: BasePlayer):
        self.board = Board()
        self.first_players_turn = True
        self.move_number = 0
        self.players = [player1, player2]

    def execute_turn(self) -> None:
        """Ask the next player for their next turn after providing them with the board state."""
        if self.first_players_turn:
            current_player = self.players[0]
        else:
            current_player = self.players[1]

        try:
            self.play_next_move(current_player)
        except ColumnFullError:
            print(f"Invalid move, try again.")
            self.execute_turn()

        self.first_players_turn = not self.first_players_turn

    def play_next_move(self, current_player: BasePlayer):
        move = current_player.get_move(self.board)
        self.board.add_token(move.token_type, move.column_number)

    def display_board(self):
        self.board.show_board()
