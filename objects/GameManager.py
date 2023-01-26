import time

from objects.Game import Game
from players.BasePlayer import BasePlayer


class GameManager(object):
    """A class that will conduct a match, asking players for moves, validating the moves, and determining result."""

    def __init__(self, player1: BasePlayer, player2: BasePlayer):
        # store the game and player references
        self.game = Game(player1, player2)

    def run_game(self):
        for x in range(42):
            self.game.execute_turn()
            self.game.display_board()
            time.sleep(0.5)
