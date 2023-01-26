
class Error(Exception):
    """A base class for custom exceptions."""
    pass


class ColumnFullError(Error):
    """An exception that is raised when a column is full."""

    def __init__(self, column_number: int):
        self.column_number = column_number
        self.message = f"Column {column_number} is full."
        super().__init__(self.message)
