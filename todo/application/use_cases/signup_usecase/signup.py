import typing


class User(typing.Protocol):
    """User Interface."""

    def signup(self, name: str, email: str, password: str) -> None: ...
