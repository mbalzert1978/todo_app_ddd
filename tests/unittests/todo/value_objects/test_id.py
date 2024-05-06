import pytest

from todo.domain.roots.todo.exception import WrongType
from todo.domain.roots.todo.value_objects.uuid_id import UuidId


def test_uuid_id_generate_valid_uuid() -> None:
    uid = UuidId.generate()
    assert uid.value == UuidId.from_value(uid.value).value


def test_uuid_id_from_value_wrong_type() -> None:
    with pytest.raises(WrongType):
        UuidId.from_value(42)  # type: ignore[arg-type]
