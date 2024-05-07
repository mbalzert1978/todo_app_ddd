import dataclasses

from todo.domain.todo.exception import EmptyError
from todo.shared_kernel.utils import is_empty
from todo.shared_kernel.valueobject import ValueObject


@dataclasses.dataclass(frozen=True, slots=True)
class Title(ValueObject[str]):
    value: str

    @classmethod
    def new(cls, value: str) -> "Title":
        if is_empty(value):
            raise EmptyError("title", value)
        return cls(value)
