import dataclasses

from todo.domain.entities.shared.entity import Entity
from todo.domain.entities.user.user_id import UserId
from todo.domain.entities.user.user_name import UserName


@dataclasses.dataclass
class User(Entity):
    id: UserId
    name: UserName

    @classmethod
    def create(cls, id: UserId, name: UserName) -> "User":
        return cls(id=id, name=name)
