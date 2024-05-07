import datetime as dt

import pytest

from todo.shared_kernel.utils import get_utc_now, is_empty


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


def test_get_utc_now_should_return_dt_object_with_tzinfo_utc() -> None:
    result = get_utc_now()

    assert isinstance(result, dt.datetime)
    assert result.tzinfo == dt.timezone.utc
