class TodoError(Exception):
    """Base Todo Error class for other exceptions"""


class EmptyError(TodoError):
    """Raised when an value is empty."""

    def __init__(self, attr: str, value: str | None) -> None:
        self.attr = attr
        self.value = value
        super().__init__(f"{self.attr.capitalize()} cannot be empty: {self.value}")


class WrongType(TodoError):
    """Raised when an object is of the wrong type."""
