import dataclasses
import typing


@dataclasses.dataclass(frozen=True)
class ValueObject:
    value: typing.Any

    def __eq__(self, __value: object) -> bool:
        return isinstance(__value, type(self)) and self.value == __value

    def __hash__(self) -> int:
        if isinstance(self.value, typing.Iterable):
            return hash(hash(v) for v in self.value)
        return hash(self.value)
