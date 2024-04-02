import datetime as dt

import pytest

from todo.domain.abstractions.datetime import DateTimeProvider
from todo.domain.entities.shared.utils import get_utc_now, is_empty


@pytest.mark.parametrize(
    ["value", "expected", "identifier"],
    [
        ("", True, "empty string"),
        (" ", True, "withespace"),
        ("     ", True, "multiple whitespaces in string"),
        (None, True, "None value"),
        ([], True, "empty list"),
        (0, True, "zero value"),
    ],
)
def test_is_empty_string_when_empty_input_string_should_return_true(
    value,
    expected,
    identifier,
):
    assert is_empty(value) == expected, identifier


@pytest.mark.parametrize(
    ["value", "expected", "identifier"],
    [
        ("foo", False, "no empty string"),
        (" foo ", False, "leading whitespace in string"),
        (["foo"], False, "no empty list"),
        (1, False, "no zero value"),
    ],
)
def test_is_empty_string_when_correct_input_string_should_return_false(
    value,
    expected,
    identifier,
):
    assert is_empty(value) == expected, identifier


def test_get_utc_now_when_provider_given_should_call_now_with_correct_timezone():
    class StubDateTimeProvider(DateTimeProvider):
        def now(self, tzinfo: dt.tzinfo | None = None) -> dt.datetime:
            self._tz = tzinfo
            return expected_time

    expected_time = dt.datetime(2022, 1, 1, 0, 0, 0)
    stub = StubDateTimeProvider()

    result = get_utc_now(provider=stub)

    assert result == expected_time
    assert stub._tz == dt.timezone.utc
