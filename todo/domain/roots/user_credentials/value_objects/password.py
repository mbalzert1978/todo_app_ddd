import dataclasses

from todo.domain.abstractions.hashing import HashingProvider
from todo.domain.abstractions.validation import PasswordValidationProvider
from todo.domain.roots.user_credentials.exception import (
    EmptyError,
    InvalidPasswordError,
)
from todo.shared_kernel.utils import is_empty
from todo.shared_kernel.valueobject import ValueObject

from .password_hash import PasswordHash


@dataclasses.dataclass(frozen=True, slots=True)
class Password(ValueObject):
    value: str

    @classmethod
    def new(cls, value: str, provider: PasswordValidationProvider) -> "Password":
        if is_empty(value):
            raise EmptyError("Password", value)
        if provider.is_valid_password(value):
            return cls(value)
        raise InvalidPasswordError(value)

    def to_hash(self, salt: str, provider: HashingProvider) -> PasswordHash:
        return PasswordHash.create(self.value, salt, provider)
