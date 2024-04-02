import datetime as dt
from unittest.mock import MagicMock

import pytest

from todo.domain.abstractions.datetime import DateTimeProvider
from todo.domain.entities.shared.utils import get_utc_now, is_empty_string


@pytest.mark.parametrize(
    ["value", "expected", "identifier"],
    [
        ("", True, "empty string"),
        (" ", True, "empty string and withespace"),
        ("     ", True, "multiple whitespaces in string"),
        (None, True, "None value"),
    ],
)
def test_is_empty_string_when_empty_input_string_should_return_true(
    value,
    expected,
    identifier,
):
    assert is_empty_string(value) == expected, identifier


@pytest.mark.parametrize(
    ["value", "expected", "identifier"],
    [
        ("foo", False, "no empty string"),
        (" foo ", False, "leading whitespace in string"),
    ],
)
def test_is_empty_string_when_correct_input_string_should_return_false(
    value,
    expected,
    identifier,
):
    assert is_empty_string(value) == expected, identifier


def test_get_utc_now_when_provider_given_should_call_now_with_correct_timezone():
    # Arrange
    class StubDateTimeProvider(DateTimeProvider):
        def now(self, tzinfo: dt.tzinfo | None = None) -> dt.datetime:
            self._tz = tzinfo
            return expected_time

    expected_time = dt.datetime(2022, 1, 1, 0, 0, 0)
    stub = StubDateTimeProvider()

    # Act
    result = get_utc_now(provider=stub)

    # Assert
    assert result == expected_time
    assert stub._tz == dt.timezone.utc
