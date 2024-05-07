import dataclasses

from todo.shared_kernel.uuid_id import UuidId
from todo.shared_kernel.valueobject import ValueObject

DEFAULT_FN = UuidId.generate

@dataclasses.dataclass
class Entity:
    id: ValueObject = dataclasses.field(default_factory=DEFAULT_FN)

    def __eq__(self, __value: object) -> bool:
        return isinstance(__value, type(self)) and self.id == __value.id

    def __hash__(self) -> int:
        return hash(self)
