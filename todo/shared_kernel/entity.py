import dataclasses

from .valueobject import ValueObject


@dataclasses.dataclass
class Entity:
    id: ValueObject

    def __eq__(self, __value: object) -> bool:
        return isinstance(__value, type(self)) and self.id == __value.id

    def __hash__(self) -> int:
        return hash(self)
