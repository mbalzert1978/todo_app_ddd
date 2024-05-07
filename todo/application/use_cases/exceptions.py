class UseCaseError(Exception):
    """Base Todo UseCaseError class for other exceptions"""


class EmailInUseError(UseCaseError):
    """Raised when an email is already in use."""


class NotFoundError(UseCaseError):
    """Raised when an object is not found."""


class TransactionError(UseCaseError):
    """Raised when a transaction fails."""

    def __init__(self, email: str, *args: object) -> None:
        self.email = email
        super().__init__(*args)


class CredentialsError(UseCaseError):
    """Raised when a password is invalid."""
