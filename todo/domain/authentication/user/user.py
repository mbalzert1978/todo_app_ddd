import dataclasses

from todo.domain.authentication.user.user_id import UserId
from todo.domain.authentication.user.user_name import UserName
from todo.domain.authentication.user_credentials.email import Email
from todo.shared_kernel.entity import Entity


@dataclasses.dataclass
class User(Entity):
    name: UserName
    email: Email

    @classmethod
    def new(cls, name: UserName, email: Email) -> "User":
        return cls(id=UserId.generate(), name=name, email=email)
