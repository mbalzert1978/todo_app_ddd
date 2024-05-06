import dataclasses

from todo.domain.roots.user.value_objects.user_id import UserId
from todo.domain.roots.user.value_objects.user_name import UserName
from todo.shared_kernel.entity import Entity


@dataclasses.dataclass
class User(Entity):
    name: UserName

    @classmethod
    def new(cls, name: UserName) -> "User":
        return cls(id=UserId.generate(), name=name)
