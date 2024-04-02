import dataclasses

from todo.domain.entities.shared.exceptions import EmptyError
from todo.domain.entities.shared.utils import is_empty_str
from todo.domain.entities.shared.valueobject import ValueObject


@dataclasses.dataclass(frozen=True)
class UserName(ValueObject):
    value: str

    @classmethod
    def create(cls, value: str) -> "UserName":
        if is_empty_str(value):
            raise EmptyError("user name", value)
        return cls(value)
