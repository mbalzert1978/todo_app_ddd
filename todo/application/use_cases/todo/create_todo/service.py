import datetime

from todo.application.use_cases.exceptions import NotFoundError
from todo.domain.authentication.abstraction.repository import UserRepository
from todo.domain.todo.description import Description
from todo.domain.todo.due_date import DueDate
from todo.domain.todo.title import Title
from todo.domain.todo.todo import Todo


class TodoService:
    def __init__(self, users: UserRepository) -> None:
        self.users = users

    def create(
        self,
        email: str,
        title: str,
        description: str,
        duedate: datetime.datetime,
    ) -> None:
        if (user := self.users.get_by_email(email)) is None:
            raise NotFoundError()

        user.add_todo(
            Todo.new(
                user.id,
                Title.new(title),
                Description.new(description),
                DueDate.new(duedate),
            )
        )
