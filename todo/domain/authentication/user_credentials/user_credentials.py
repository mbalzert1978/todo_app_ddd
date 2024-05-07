import dataclasses
import typing

from todo.domain.authentication.abstraction.hashing import HashingProvider
from todo.domain.authentication.user_credentials.password import Password
from todo.domain.authentication.user_credentials.password_hash import (
    PasswordHash,
)
from todo.shared_kernel.entity import Entity
from todo.shared_kernel.uuid_id import UuidId
from todo.shared_kernel.valueobject import ValueObject

T = typing.TypeVar("T")


@dataclasses.dataclass(kw_only=True)
class UserCredentials(Entity, typing.Generic[T]):
    user_id: ValueObject[T]
    password_hash: PasswordHash

    @classmethod
    def new(
        cls, user_id: ValueObject[T], password_hash: PasswordHash
    ) -> "UserCredentials":
        return cls(id=UuidId.generate(), user_id=user_id, password_hash=password_hash)

    def set_password(
        self,
        password: Password,
        salt: str,
        provider: HashingProvider,
    ) -> None:
        self.password_hash = password.to_hash(salt, provider)
