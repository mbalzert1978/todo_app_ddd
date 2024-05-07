from todo.application.use_cases.exceptions import CredentialsError, NotFoundError
from todo.domain.authentication.abstraction.hashing import HashingProvider
from todo.domain.authentication.abstraction.repository import UserRepository
from todo.domain.authentication.user.user import User


class LoginService:
    def __init__(self, hash_provider: HashingProvider, users: UserRepository) -> None:
        self.hasher = hash_provider
        self.users = users

    def login(self, email: str, password: str) -> User:
        if (user := self.users.get_by_email(email)) is None:
            raise NotFoundError()
        if not user.password_hash.verify(password, self.hasher):
            raise CredentialsError()
        return user
