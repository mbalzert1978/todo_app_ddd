import typing

from todo.domain.authentication.user.user import User
from todo.domain.authentication.user_credentials.user_credentials import UserCredentials


class UserRepository(typing.Protocol):
    """User Repository Interface."""

    def __enter__(self) -> typing.Self: ...
    def __exit__(self, exc_type, exc_val, exc_tb) -> None: ...

    def add(self, user: User) -> None: ...
    def get_by_id(self, user_id: str) -> typing.Optional[User]: ...
    def get_by_email(self, email: str) -> typing.Optional[User]: ...


class UserCredentialRepository(typing.Protocol):
    """User Credential Repository Interface."""

    def __enter__(self) -> typing.Self: ...
    def __exit__(self, exc_type, exc_val, exc_tb) -> None: ...
    def add(self, user_credential: UserCredentials) -> None: ...
    def get_by_email(self, email: str) -> typing.Optional[UserCredentials]: ...