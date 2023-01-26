import random

from objects.Move import Move
from players.BasePlayer import BasePlayer


class RandomPlayer(BasePlayer):
    """A player that chooses a random column to play in."""

    def get_move(self, board_state):
        return Move(random.randrange(1, 8), self.token_type)
