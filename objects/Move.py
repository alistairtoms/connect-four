class Move:
    """Class to represent a move."""

    def __init__(self, column_number: int, token_type: str):
        self.column_number = column_number
        self.token_type = token_type
