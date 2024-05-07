import bcrypt


class BcryptHasher:
    def generate_salt(self) -> bytes:
        """Generate a random salt."""
        return bcrypt.gensalt(12)

    def hash(self, password: str, salt: bytes) -> bytes:
        """Generate a hash for the given password and salt."""
        return bcrypt.hashpw(password.encode(), salt)

    def verify(self, password: str, hash: bytes) -> bool:
        """Verify that the given hash matches the given password and salt."""
        return bcrypt.checkpw(password.encode(), hash)
