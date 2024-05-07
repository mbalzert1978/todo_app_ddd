import typing


class EmailValidationProvider(typing.Protocol):
    """Email Validation Provider Interface."""

    def is_valid_email(self, email: str) -> bool:
        """Validate Email."""


class PasswordValidationProvider(typing.Protocol):
    """Password Validation Provider Interface."""

    def is_valid_password(self, password: str) -> bool:
        """Validate Password."""


class ValidationProvider(typing.Protocol):
    """Validation Provider Interface."""

    @property
    def email(self) -> EmailValidationProvider:
        """Email Validation Provider."""

    @property
    def password(self) -> PasswordValidationProvider:
        """Password Validation Provider."""
