import dataclasses

from todo.shared_kernel.uuid_id import UuidId


@dataclasses.dataclass(frozen=True, slots=True)
class TodoId(UuidId):
    """TodoId."""
