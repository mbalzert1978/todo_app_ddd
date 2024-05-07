import dataclasses
import typing

from todo.domain.authentication.user.email import Email
from todo.domain.authentication.user.password_hash import PasswordHash
from todo.domain.authentication.user.user_id import UserId
from todo.domain.authentication.user.user_name import UserName
from todo.domain.todo.todo import Todo
from todo.shared_kernel.entity import Entity

T = typing.TypeVar("T")


@dataclasses.dataclass(kw_only=True, eq=False, slots=True)
class User(Entity):
    name: UserName
    email: Email
    password_hash: PasswordHash
    todos: set[Todo] = dataclasses.field(default_factory=set)

    @classmethod
    def new(cls, name: UserName, email: Email, password_hash: PasswordHash) -> "User":
        return cls(
            id=UserId.generate(),
            name=name,
            email=email,
            password_hash=password_hash,
        )

    def add_todo(self, todo: Todo) -> None:
        self.todos.add(todo)

    def remove_todo(self, todo: Todo) -> None:
        self.todos.remove(todo)

    def get_todo(self, filter: typing.Callable[[Todo], bool], default: T) -> Todo | T:
        return next((todo for todo in self.todos if filter(todo)), default)
