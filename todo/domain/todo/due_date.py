import dataclasses
import datetime

from todo.domain.todo.exception import WrongType
from todo.shared_kernel.utils import get_utc_now
from todo.shared_kernel.valueobject import ValueObject


@dataclasses.dataclass(frozen=True, slots=True)
class DueDate(ValueObject[datetime.datetime]):
    value: datetime.datetime

    @classmethod
    def new(cls, value: datetime.datetime) -> "DueDate":
        if isinstance(value, datetime.datetime):
            return cls(value)
        msg = f"DueDate must be of type {type(datetime.datetime)}, not {type(value)}"
        raise WrongType(msg)

    @property
    def date(self) -> datetime.date:
        return self.value.date()

    @property
    def time(self) -> datetime.time:
        return self.value.time()

    @property
    def has_past(self) -> bool:
        return self.value < get_utc_now()

    @property
    def is_future(self) -> bool:
        return self.value > get_utc_now()
