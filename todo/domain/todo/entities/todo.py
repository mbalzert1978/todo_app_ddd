import dataclasses
import datetime as dt

from todo.domain.roots.todo.value_objects.description import Description
from todo.domain.roots.todo.value_objects.due_date import DueDate
from todo.domain.roots.todo.value_objects.title import Title
from todo.domain.roots.todo.value_objects.todo_id import TodoId
from todo.shared_kernel.entity import Entity
from todo.shared_kernel.utils import get_utc_now


@dataclasses.dataclass(slots=True)
class Todo(Entity):
    title: Title
    description: Description
    due_date: DueDate
    completed: bool
    created_at: dt.datetime
    updated_at: dt.datetime

    @classmethod
    def new(
        cls,
        title: Title,
        description: Description,
        due_date: DueDate,
    ) -> "Todo":
        now = get_utc_now()
        return cls(
            id=TodoId.generate(),
            title=title,
            description=description,
            due_date=due_date,
            completed=False,
            created_at=now,
            updated_at=now,
        )

    def complete(self) -> "Todo":
        return dataclasses.replace(self, completed=True, updated_at=get_utc_now())

    def uncompleted(self) -> "Todo":
        return dataclasses.replace(self, completed=False, updated_at=get_utc_now())

    def set_due_date(self, due_date: DueDate) -> "Todo":
        return dataclasses.replace(self, due_date=due_date, updated_at=get_utc_now())

    def set_title(self, title: Title) -> "Todo":
        return dataclasses.replace(self, title=title, updated_at=get_utc_now())

    def set_description(self, description: Description) -> "Todo":
        return dataclasses.replace(
            self,
            description=description,
            updated_at=get_utc_now(),
        )
