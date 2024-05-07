import dataclasses

from todo.domain.todo.exception import EmptyError
from todo.shared_kernel.utils import is_empty
from todo.shared_kernel.valueobject import ValueObject


@dataclasses.dataclass(frozen=True, slots=True)
class Description(ValueObject[str]):
    value: str

    @classmethod
    def new(cls, value: str) -> "Description":
        if is_empty(value):
            raise EmptyError("description", value)
        return cls(value)
