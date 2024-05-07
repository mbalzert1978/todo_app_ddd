import typing

from todo.domain.authentication.user.user import User


class TokenProvider(typing.Protocol):
    def generate_token(self, user: User) -> str: ...
