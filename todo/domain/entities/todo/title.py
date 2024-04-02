import dataclasses

from todo.domain.entities.shared.exceptions import EmptyError
from todo.domain.entities.shared.utils import is_empty
from todo.domain.entities.shared.valueobject import ValueObject


@dataclasses.dataclass(frozen=True)
class Title(ValueObject):
    value: str

    @classmethod
    def create(cls, value: str) -> "Title":
        if is_empty(value):
            raise EmptyError("title", value)
        return cls(value)
