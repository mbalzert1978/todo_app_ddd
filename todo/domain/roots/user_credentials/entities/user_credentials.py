import dataclasses

from todo.domain.abstractions.hashing import HashingProvider
from todo.domain.entities.user.user_id import UserId
from todo.domain.entities.user_credentials.email import Email
from todo.domain.entities.user_credentials.password import Password
from todo.domain.entities.user_credentials.password_hash import PasswordHash
from todo.shared_kernel.entity import Entity


@dataclasses.dataclass
class UserCredentials(Entity):
    user_id: UserId
    email: Email
    password_hash: PasswordHash

    def set_password(
        self,
        password: Password,
        salt: str,
        provider: HashingProvider,
    ) -> None:
        self.password_hash = password.to_hash(salt, provider)
