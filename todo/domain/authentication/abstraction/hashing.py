import typing


class HashingProvider(typing.Protocol):
    def generate_salt(self) -> str:
        """Generate a random salt."""

    def hash(self, password: str, salt: str) -> str:
        """Generate a hash for the given password and salt."""

    def verify(self, password: str, salt: str, hash: str) -> bool:
        """Verify that the given hash matches the given password and salt."""
