import dataclasses

from todo.domain.abstractions.hashing import HashingProvider
from todo.domain.authentication.user.value_objects.user_id import UserId
from todo.domain.authentication.user_credentials.value_objects.email import Email
from todo.domain.authentication.user_credentials.value_objects.password import Password
from todo.domain.authentication.user_credentials.value_objects.password_hash import (
    PasswordHash,
)
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
