class UserCredentialsError(Exception):
    """Base UserCredentials Error class for other exceptions"""


class InvalidEmailError(UserCredentialsError):
    """Raised when an email is invalid"""

    def __init__(self, value: str) -> None:
        self.value = value
        super().__init__(f"{self.value} is not a valid email.")


class InvalidPasswordError(UserCredentialsError):
    """Raised when an password is invalid"""

    def __init__(self, value: str) -> None:
        self.value = value
        super().__init__(f"{self.value} is not a valid password.")


class EmptyError(UserCredentialsError):
    """Raised when an value is empty."""

    def __init__(self, attr: str, value: str | None) -> None:
        self.attr = attr
        self.value = value
        super().__init__(f"{self.attr.capitalize()} cannot be empty: {self.value}")
