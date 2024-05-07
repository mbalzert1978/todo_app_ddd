import dataclasses

from todo.domain.authentication.abstraction.hashing import HashingProvider
from todo.shared_kernel.valueobject import ValueObject


@dataclasses.dataclass(frozen=True, slots=True)
class PasswordHash(ValueObject):
    value: str
    _salt: str
    _provider: HashingProvider

    @classmethod
    def create(
        cls,
        password: str,
        salt: str,
        provider: HashingProvider,
    ) -> "PasswordHash":
        value = provider.hash(password, salt)
        return cls(value, salt, provider)

    def verify(self, password: str) -> bool:
        return self._provider.verify(password, self._salt, self.value)
