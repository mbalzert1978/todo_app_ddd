import datetime as dt
import typing


def get_utc_now() -> dt.datetime:
    return dt.datetime.now(dt.timezone.utc)


def is_nothing(value: typing.Any | None) -> bool:
    return not value or value is None


def is_empty_str(value: typing.Any | None) -> bool:
    return isinstance(value, str) and value.isspace()
