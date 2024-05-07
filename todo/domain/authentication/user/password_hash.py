import dataclasses

from todo.domain.authentication.abstraction.hashing import HashingProvider
from todo.shared_kernel.valueobject import ValueObject


@dataclasses.dataclass(frozen=True, slots=True)
class PasswordHash(ValueObject):
    value: bytes

    @classmethod
    def new(
        cls,
        password: str,
        salt: bytes,
        provider: HashingProvider,
    ) -> "PasswordHash":
        value = provider.hash(password, salt)
        return cls(value)

    def verify(self, password: str, provider: HashingProvider) -> bool:
        return provider.verify(password, self.value)
