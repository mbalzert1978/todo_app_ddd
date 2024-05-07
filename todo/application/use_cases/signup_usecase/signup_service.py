from todo.application.use_cases.exceptions import EmailInUseError
from todo.domain.authentication.abstraction.hashing import HashingProvider
from todo.domain.authentication.abstraction.repository import UserRepository
from todo.domain.authentication.abstraction.validation import ValidationProvider
from todo.domain.authentication.user.email import Email
from todo.domain.authentication.user.password import Password
from todo.domain.authentication.user.password_hash import PasswordHash
from todo.domain.authentication.user.user import User
from todo.domain.authentication.user.user_name import UserName


class SignUpService:
    def __init__(
        self,
        hash_provider: HashingProvider,
        validation_provider: ValidationProvider,
        users: UserRepository,
    ) -> None:
        self.hasher = hash_provider
        self.validator = validation_provider
        self.users = users

    def sign_up(self, name: str, email: str, password: str) -> None:
        if self.users.get_by_email(email) is not None:
            raise EmailInUseError()

        user_name = UserName.new(name)
        user_email = Email.new(email, self.validator.email)
        user_password = Password.new(password, self.validator.password)
        password_hash = PasswordHash.new(
            user_password.value,
            self.hasher.generate_salt(),
            self.hasher,
        )

        user = User.new(name=user_name, email=user_email, password_hash=password_hash)

        with self.users as users:
            users.add(user)
