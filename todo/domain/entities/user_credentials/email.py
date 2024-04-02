import dataclasses

from todo.domain.abstractions.validation import EmailValidationProvider
from todo.domain.entities.shared.exceptions import EmptyError
from todo.domain.entities.shared.utils import is_empty_str
from todo.domain.entities.shared.valueobject import ValueObject
from todo.domain.entities.user_credentials.exception import InvalidEmailError


@dataclasses.dataclass(frozen=True)
class Email(ValueObject):
    value: str

    @classmethod
    def create(cls, value: str, provider: EmailValidationProvider) -> "Email":
        if is_empty_str(value):
            raise EmptyError("email", value)
        if not provider.is_valid_email(value):
            raise InvalidEmailError(value)
        return cls(value)
