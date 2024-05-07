from todo.application.use_cases.exceptions import EmailInUseError
from todo.domain.authentication.abstraction.hashing import HashingProvider
from todo.domain.authentication.abstraction.repository import (
    UserCredentialRepository,
    UserRepository,
)
from todo.domain.authentication.abstraction.validation import ValidationProvider
from todo.domain.authentication.user.email import Email
from todo.domain.authentication.user.user import User
from todo.domain.authentication.user.user_name import UserName
from todo.domain.authentication.user_credentials.password_hash import PasswordHash
from todo.domain.authentication.user_credentials.user_credentials import UserCredentials


class SignUpService:
    def __init__(
        self,
        hash_provider: HashingProvider,
        validation_provider: ValidationProvider,
        users: UserRepository,
        credentials: UserCredentialRepository,
    ) -> None:
        self.hasher = hash_provider
        self.validator = validation_provider
        self.users = users
        self.credentials = credentials

    def sign_up(self, name: str, email: str, password: str) -> None:
        if self.users.get_by_email(email) is not None:
            raise EmailInUseError()

        user_name = UserName.new(name)
        user_email = Email.new(email, self.validator.email)

        user = User.new(name=user_name, email=user_email)

        salt = self.hasher.generate_salt()
        password_hash = PasswordHash.new(password, salt, self.hasher)

        user_credentials = UserCredentials.new(
            user_id=user.id, password_hash=password_hash
        )

        with self.users as users, self.credentials as credentials:
            users.add(user)
            credentials.add(user_credentials)
