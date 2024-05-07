from todo.application.use_cases.exceptions import (
    CredentialsError,
    NotFoundError,
    TransactionError,
)
from todo.domain.authentication.abstraction.hashing import HashingProvider
from todo.domain.authentication.abstraction.repository import (
    UserCredentialRepository,
    UserRepository,
)
from todo.domain.authentication.user.user import User


class LoginService:
    def __init__(
        self,
        hash_provider: HashingProvider,
        users: UserRepository,
        credentials: UserCredentialRepository,
    ) -> None:
        self.hasher = hash_provider
        self.users = users
        self.credentials = credentials

    def login(self, email: str, password: str) -> User:
        if (user := self.users.get_by_email(email)) is None:
            raise NotFoundError()
        if (credentials := self.credentials.get_by_id(user.id)) is None:
            raise TransactionError(email)
        if not credentials.password_hash.verify(password, self.hasher):
            raise CredentialsError()
        return user
