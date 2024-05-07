import dataclasses

from todo.domain.authentication.abstraction.validation import EmailValidationProvider
from todo.domain.authentication.user.exception import EmptyError
from todo.domain.authentication.user_credentials.exception import InvalidEmailError
from todo.shared_kernel.utils import is_empty
from todo.shared_kernel.valueobject import ValueObject


@dataclasses.dataclass(frozen=True, slots=True)
class Email(ValueObject):
    value: str

    @classmethod
    def new(cls, value: str, provider: EmailValidationProvider) -> "Email":
        if is_empty(value):
            raise EmptyError("Email", value)
        if provider.is_valid_email(value):
            return cls(value)
        raise InvalidEmailError(value)
