import string

import pydantic

from todo.domain.authentication.abstraction.validation import (
    EmailValidationProvider,
    PasswordValidationProvider,
)


class PydanticEmailValidator:
    """Email Validation Provider Interface."""

    def is_valid_email(self, email: str) -> bool:
        """Validate Email."""

        class _Email(pydantic.BaseModel):
            email: pydantic.EmailStr

        try:
            _Email(email=email)
        except pydantic.ValidationError:
            return False
        else:
            return True


class PasswordValidator:
    """Password Validation Provider Interface."""

    def is_valid_password(self, password: str) -> bool:
        """Validate Password."""
        if (
            len(password) < 8
            or not any(char.isdigit() for char in password)
            or not any(char in string.punctuation for char in password)
        ):
            return False
        return True


class PydanticValidator:
    @property
    def email(self) -> EmailValidationProvider:
        """Email Validation Provider."""
        return PydanticEmailValidator()

    @property
    def password(self) -> PasswordValidationProvider:
        """Password Validation Provider."""
        return PasswordValidator()
