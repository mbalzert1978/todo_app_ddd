import dataclasses

from todo.domain.entities.shared.exceptions import EmptyError
from todo.domain.entities.shared.utils import is_empty
from todo.domain.entities.shared.valueobject import ValueObject


@dataclasses.dataclass(frozen=True)
class Description(ValueObject):
    value: str

    @classmethod
    def create(cls, value: str) -> "Description":
        if is_empty(value):
            raise EmptyError("description", value)
        return cls(value)
