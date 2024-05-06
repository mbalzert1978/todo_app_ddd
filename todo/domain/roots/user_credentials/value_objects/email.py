import dataclasses

from todo.domain.abstractions.validation import EmailValidationProvider
from todo.domain.roots.user_credentials.exception import EmptyError, InvalidEmailError
from todo.shared_kernel.utils import is_empty
from todo.shared_kernel.valueobject import ValueObject


@dataclasses.dataclass(frozen=True, slots=True)
class Email(ValueObject):
    value: str

    @classmethod
    def create(cls, value: str, provider: EmailValidationProvider) -> "Email":
        if is_empty(value):
            raise EmptyError("email", value)
        if provider.is_valid_email(value):
            return cls(value)
        raise InvalidEmailError(value)
