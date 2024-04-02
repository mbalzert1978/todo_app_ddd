import datetime as dt
import typing


class DateTimeProvider(typing.Protocol):
    def now(self, tzinfo: dt.tzinfo | None = None) -> dt.datetime:
        """Returns the current time in UTC"""
