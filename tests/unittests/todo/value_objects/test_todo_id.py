import pytest

from todo.domain.todo.exception import WrongType
from todo.domain.todo.value_objects.todo_id import TodoId


def test_uuid_id_generate_valid_uuid() -> None:
    uid = TodoId.generate()
    assert uid.value == TodoId.new(uid.value).value


def test_uuid_id_from_value_wrong_type() -> None:
    with pytest.raises(WrongType):
        TodoId.new(42)  # type: ignore[arg-type]
