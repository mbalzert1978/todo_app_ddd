import typing

from todo.domain.authentication.user_credentials.user_credentials import UserCredentials
from todo.shared_kernel.valueobject import ValueObject


class UserCredentialRepository:
    """User Credential Repository Interface."""

    def __init__(self) -> None:
        self.credentials: set[UserCredentials] = set()
        self.next: typing.Optional[UserCredentials] = None

    def __enter__(self) -> typing.Self:
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        if exc_type is not None:
            self.rollback()
            raise exc_type from exc_val
        self.commit()

    def add(self, user_credential: UserCredentials) -> None:
        self.next = user_credential

    def get_by_id(self, user_id: ValueObject) -> typing.Optional[UserCredentials]:
        return next(
            (credential for credential in self.credentials if credential.id == user_id),
            None,
        )

    def rollback(self) -> None:
        self.next = None

    def commit(self) -> None:
        if self.next is None:
            return
        self.credentials.add(self.next)
        self.next = None
