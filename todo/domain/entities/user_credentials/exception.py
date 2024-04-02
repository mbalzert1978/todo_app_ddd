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
