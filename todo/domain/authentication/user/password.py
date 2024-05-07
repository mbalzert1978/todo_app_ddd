import dataclasses

from todo.domain.authentication.abstraction.hashing import HashingProvider
from todo.domain.authentication.abstraction.validation import PasswordValidationProvider
from todo.domain.authentication.user.exception import InvalidPasswordError
from todo.domain.authentication.user.password_hash import PasswordHash
from todo.shared_kernel.valueobject import ValueObject


@dataclasses.dataclass(frozen=True, slots=True)
class Password(ValueObject):
    value: str

    @classmethod
    def new(cls, value: str, provider: PasswordValidationProvider) -> "Password":
        if provider.is_valid_password(value):
            return cls(value)
        raise InvalidPasswordError(value)

    def to_hash(self, salt: bytes, provider: HashingProvider) -> PasswordHash:
        return PasswordHash.new(self.value, salt, provider)
