import typing

from todo.domain.authentication.user.user import User


class UserRepository:
    """User Repository Interface."""

    def __init__(self) -> None:
        self.users: set[User] = set()
        self.next: typing.Optional[User] = None

    def __enter__(self) -> typing.Self:
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        if exc_type is not None:
            self.rollback()
            raise exc_type from exc_val
        self.commit()

    def add(self, user: User) -> None:
        self.next = user

    def get_by_email(self, email: str) -> typing.Optional[User]:
        return next((user for user in self.users if user.email.value == email), None)

    def rollback(self) -> None:
        self.next = None

    def commit(self) -> None:
        if self.next is None:
            return
        self.users.add(self.next)
        self.next = None
