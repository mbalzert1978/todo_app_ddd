class UserError(Exception):
    """Base Todo Error class for other exceptions"""


class InvalidEmailError(UserError):
    """Raised when an email is invalid"""

    def __init__(self, value: str) -> None:
        self.value = value
        super().__init__(f"{self.value} is not a valid email.")


class InvalidPasswordError(UserError):
    """Raised when an password is invalid"""

    def __init__(self, value: str) -> None:
        self.value = value
        super().__init__(f"{self.value} is not a valid password.")
