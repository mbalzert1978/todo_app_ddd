import dataclasses

from todo.domain.authentication.user_credentials.abstraction.hashing import (
    HashingProvider,
)
from todo.domain.authentication.user_credentials.email import Email
from todo.domain.authentication.user_credentials.password import Password
from todo.domain.authentication.user_credentials.password_hash import (
    PasswordHash,
)
from todo.shared_kernel.entity import Entity
from todo.shared_kernel.uuid_id import UuidId


@dataclasses.dataclass
class UserCredentials(Entity):
    user_id: UuidId
    email: Email
    password_hash: PasswordHash

    def set_password(
        self,
        password: Password,
        salt: str,
        provider: HashingProvider,
    ) -> None:
        self.password_hash = password.to_hash(salt, provider)
