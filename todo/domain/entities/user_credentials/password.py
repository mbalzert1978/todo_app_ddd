import dataclasses

from todo.domain.abstractions.hashing import HashingProvider
from todo.domain.abstractions.validation import PasswordValidationProvider
from todo.domain.entities.shared.exceptions import EmptyError
from todo.domain.entities.shared.utils import is_empty_str
from todo.domain.entities.shared.valueobject import ValueObject
from todo.domain.entities.user_credentials.exception import InvalidPasswordError
from todo.domain.entities.user_credentials.password_hash import PasswordHash


@dataclasses.dataclass(frozen=True)
class Password(ValueObject):
    value: str

    @classmethod
    def create(cls, value: str, provider: PasswordValidationProvider) -> "Password":
        if is_empty_str(value):
            raise EmptyError("Password", value)
        if not provider.is_valid_password(value):
            raise InvalidPasswordError(value)
        return cls(value)

    def to_hash(self, salt: str, provider: HashingProvider) -> PasswordHash:
        return PasswordHash.create(self.value, salt, provider)
