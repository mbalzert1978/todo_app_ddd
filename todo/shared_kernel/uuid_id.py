import dataclasses
import typing
import uuid

from todo.domain.todo.exception import WrongType
from todo.shared_kernel.valueobject import ValueObject


@dataclasses.dataclass(frozen=True, slots=True)
class UuidId(ValueObject[uuid.UUID]):
    value: uuid.UUID

    @classmethod
    def generate(cls) -> typing.Self:
        return cls(uuid.uuid4())

    @classmethod
    def from_str(cls, value: str) -> typing.Self:
        return cls(uuid.UUID(value))

    @classmethod
    def new(cls, value: uuid.UUID) -> typing.Self:
        if isinstance(value, uuid.UUID):
            return cls(value)
        msg = f"UuidId must be of type {uuid.UUID}, not {type(value)}"
        raise WrongType(msg)
