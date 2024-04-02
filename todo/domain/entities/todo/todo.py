import dataclasses
import datetime as dt

from todo.domain.entities.shared.entity import Entity
from todo.domain.entities.shared.utils import get_utc_now
from todo.domain.entities.todo.description import Description
from todo.domain.entities.todo.title import Title
from todo.domain.entities.todo.todo_id import TodoId


@dataclasses.dataclass
class Todo(Entity):
    title: Title
    description: Description
    completed: bool
    due_date: dt.date | None
    created_at: dt.datetime
    updated_at: dt.datetime

    @classmethod
    def create(
        cls,
        title: Title,
        description: Description,
        due_date: dt.date | None = None,
    ) -> "Todo":
        utc_now = get_utc_now()
        return cls(
            id=TodoId.create(),
            title=title,
            description=description,
            completed=False,
            due_date=due_date,
            created_at=utc_now,
            updated_at=utc_now,
        )

    def complete(self) -> "Todo":
        return dataclasses.replace(self, completed=True, updated_at=get_utc_now())

    def uncompleted(self) -> "Todo":
        return dataclasses.replace(self, completed=False, updated_at=get_utc_now())

    def set_due_date(self, due_date: dt.date) -> "Todo":
        return dataclasses.replace(self, due_date=due_date, updated_at=get_utc_now())

    def unset_due_date(self) -> "Todo":
        return dataclasses.replace(self, due_date=None, updated_at=get_utc_now())

    def set_title(self, title: Title) -> "Todo":
        return dataclasses.replace(self, title=title, updated_at=get_utc_now())

    def set_description(self, description: Description) -> "Todo":
        return dataclasses.replace(
            self,
            description=description,
            updated_at=get_utc_now(),
        )
