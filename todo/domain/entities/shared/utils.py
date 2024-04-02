import datetime as dt
import typing

from todo.domain.abstractions.datetime import DateTimeProvider


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


def is_empty_string(input_value: typing.Optional[str]) -> bool:
    """
    Checks if the input string is empty or consists only of whitespace.

    Args:
        input_value (Optional[str]): The string to check.

    Returns:
        bool: True if the string is empty or consists only of whitespace, False otherwise.
    """
    if (
        input_value is None
        or input_value == ""
        or isinstance(input_value, str)
        and input_value.isspace()
    ):
        return True
    return False
