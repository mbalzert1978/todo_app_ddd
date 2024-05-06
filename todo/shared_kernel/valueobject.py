import abc
import dataclasses
import typing

T = typing.TypeVar("T")


@dataclasses.dataclass(frozen=True, slots=True)
class ValueObject(typing.Generic[T], abc.ABC):
    value: T

    def __eq__(self, __value: object) -> bool:
        return isinstance(__value, type(self)) and self.value == __value.value

    def __hash__(self) -> int:
        if isinstance(self.value, typing.Iterable):
            return hash(hash(v) for v in self.value)
        return hash(self.value)

    @classmethod
    def from_mapping(cls, value: dict[str, T]) -> "ValueObject":
        return cls(value=value["value"])
