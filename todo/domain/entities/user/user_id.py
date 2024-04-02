import dataclasses

from todo.domain.entities.shared.id import Id


@dataclasses.dataclass(frozen=True)
class UserId(Id):
    """UserId."""
