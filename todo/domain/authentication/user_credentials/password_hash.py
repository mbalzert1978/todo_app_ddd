import dataclasses

from todo.domain.authentication.abstraction.hashing import HashingProvider
from todo.shared_kernel.valueobject import ValueObject


@dataclasses.dataclass(frozen=True, slots=True)
class PasswordHash(ValueObject):
    value: str
    _salt: str

    @classmethod
    def new(
        cls,
        password: str,
        salt: str,
        provider: HashingProvider,
    ) -> "PasswordHash":
        value = provider.hash(password, salt)
        return cls(value, salt)

    def verify(self, password: str, provider: HashingProvider) -> bool:
        return provider.verify(password, self._salt, self.value)
