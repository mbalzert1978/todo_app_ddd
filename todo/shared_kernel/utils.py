import datetime as dt
import typing

from todo.domain.abstractions.datetime import DateTimeProvider

T = typing.TypeVar("T")


def get_utc_now(provider: typing.Optional[DateTimeProvider] = None) -> dt.datetime:
    """
    Get the current UTC datetime using the given DateTimeProvider.

    Args:
        provider (Optional[DateTimeProvider]): The DateTimeProvider to use.
            If None, the built-in datetime.now function is used.

    Returns:
        datetime.datetime: The current UTC datetime.
    """
    provider = provider or dt.datetime
    return provider.now(dt.timezone.utc)


def is_empty(input_value: typing.Optional[T]) -> bool:
    """
    Checks if the input value is empty or consists only of whitespace.

    When the input value is of type integer or float, it is compared with 0.

    Args:
        input_value (Optional[T]): The value to check.

    Returns:
        bool: True if the value is empty or consists only of whitespace, False otherwise.
    """
    return (
        input_value is None
        or not input_value
        or (isinstance(input_value, str) and input_value.isspace())
    )
