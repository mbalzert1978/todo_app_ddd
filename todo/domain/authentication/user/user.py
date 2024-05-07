import dataclasses

from todo.domain.authentication.user.email import Email
from todo.domain.authentication.user.password_hash import PasswordHash
from todo.domain.authentication.user.user_id import UserId
from todo.domain.authentication.user.user_name import UserName
from todo.shared_kernel.entity import Entity


@dataclasses.dataclass(kw_only=True, eq=False, slots=True)
class User(Entity):
    name: UserName
    email: Email
    password_hash: PasswordHash

    @classmethod
    def new(cls, name: UserName, email: Email, password_hash: PasswordHash) -> "User":
        return cls(
            id=UserId.generate(),
            name=name,
            email=email,
            password_hash=password_hash,
        )
