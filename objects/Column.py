from exceptions import ColumnFullError


class Column:
    """Class that will store the tokens for one column of the board."""

    def __init__(self, number: int):
        self.tokens = [" "] * 6
        self.number = number
        self.height = 0

    def drop_token(self, token: str):
        if self.height >= 6:
            raise ColumnFullError(self.number)
        else:
            self.tokens[self.height] = token
            self.height += 1

    def print_cell(self, row: int):
        print(f"[ {self.tokens[row]} ]", end="")
