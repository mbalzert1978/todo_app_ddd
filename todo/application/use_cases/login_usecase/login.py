import typing


class User(typing.Protocol):
    """User Interface."""

    def login(self, email: str, password: str) -> None: ...
