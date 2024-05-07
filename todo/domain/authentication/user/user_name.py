import dataclasses

from todo.domain.authentication.user.exception import EmptyError
from todo.shared_kernel.utils import is_empty
from todo.shared_kernel.valueobject import ValueObject


@dataclasses.dataclass(frozen=True, slots=True)
class UserName(ValueObject):
    value: str

    @classmethod
    def new(cls, value: str) -> "UserName":
        if is_empty(value):
            raise EmptyError("UserName", value)
        return cls(value)
