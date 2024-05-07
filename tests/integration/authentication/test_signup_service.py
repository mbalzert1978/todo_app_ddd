import pytest
from todo.application.use_cases.signup_usecase.signup_service import SignUpService
from todo.domain.authentication.user.exception import InvalidEmailError, InvalidPasswordError
from todo.infrastructure.authentication.hasher import BcryptHasher
from todo.infrastructure.authentication.validator import PydanticValidator
from todo.infrastructure.persistence.memory.user import UserRepository


def setup() -> tuple[SignUpService, UserRepository]:
    ss = SignUpService(
        hash_provider=BcryptHasher(),
        validation_provider=PydanticValidator(),
        users=(user_repo := UserRepository()),
    )

    return ss, user_repo


def test_signup_service_with_correct_values_should_write_to_database() -> None:
    service, user_repo = setup()

    service.sign_up(name="test", email="test@mail.com", password="123Has-Symbols")

    assert user_repo.get_by_email("test@mail.com") is not None


def test_signup_service_with_incorrect_email_value_should_not_write_to_database() -> (
    None
):
    service, user_repo = setup()

    with pytest.raises(InvalidEmailError):
        service.sign_up(name="test", email="invaild", password="123Has-Symbols")

    with pytest.raises(InvalidPasswordError):
        service.sign_up(name="test", email="test@mail.com", password="short")

    with pytest.raises(InvalidPasswordError):
        service.sign_up(name="test", email="test@mail.com", password="nosymbols")

    assert not user_repo.users

