import abc


class BasePlayer(abc.ABC):
    """The foundations for a player class."""

    def __init__(self, token_type: str):
        self.token_type = token_type

    @abc.abstractmethod
    def get_move(self, board_state):
        pass
