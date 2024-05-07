import typing


class HashingProvider(typing.Protocol):
    def generate_salt(self) -> bytes:
        """Generate a random salt."""

    def hash(self, password: str, salt: bytes) -> bytes:
        """Generate a hash for the given password and salt."""

    def verify(self, password: str, hash: bytes) -> bool:
        """Verify that the given hash matches the given password and salt."""
