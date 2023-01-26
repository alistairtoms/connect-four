import numpy as np

from objects.Column import Column


class Board():
    """A class to store and update board layout."""

    def __init__(self):
        self.grid = [Column(x) for x in range(1,8)]

    def show_board(self):
        for row in range(5, -1, -1):
            for column in self.grid:
                column.print_cell(row)
            print("\n", end="")
        print("\n", end="")

    def add_token(self, token: str, column: int):
        self.grid[column-1].drop_token(token)
