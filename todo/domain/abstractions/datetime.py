import datetime as dt
import typing


class DateTimeProvider(typing.Protocol):
    def utc_now(self) -> dt.datetime:
        """Returns the current time in UTC"""
