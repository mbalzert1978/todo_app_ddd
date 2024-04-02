import dataclasses
import typing
import uuid

from todo.domain.entities.shared.utils import is_empty
from todo.domain.entities.shared.valueobject import ValueObject


@dataclasses.dataclass(frozen=True)
class Id(ValueObject):
    value: typing.Any

    @classmethod
    def create(cls, value: typing.Any | None = None) -> "Id":
        if is_empty(value):
            value = uuid.uuid4().hex
        return cls(value)
