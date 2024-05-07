from typing import Iterator

import pytest

from todo.application.use_cases.authentication.login_usecase.login_service import (
    LoginService,
)
from todo.application.use_cases.exceptions import CredentialsError
from todo.domain.authentication.user.email import Email
from todo.domain.authentication.user.password import Password
from todo.domain.authentication.user.password_hash import PasswordHash
from todo.domain.authentication.user.user import User
from todo.domain.authentication.user.user_name import UserName
from todo.infrastructure.authentication.hasher import BcryptHasher
from todo.infrastructure.authentication.validator import PydanticValidator
from todo.infrastructure.persistence.memory.user import UserRepository


@pytest.fixture()
def service() -> Iterator[LoginService]:
    hasher = BcryptHasher()
    pw = Password.new("test_1234", (v := PydanticValidator()).password)
    email = Email.new("test@email.com", v.email)
    pw_hash = PasswordHash.new(pw.value, hasher.generate_salt(), hasher)
    user = User.new(UserName.new("Jd"), email, pw_hash)
    service = LoginService(
        hash_provider=BcryptHasher(), users=(user_repo := UserRepository())
    )
    user_repo.add(user)
    user_repo.commit()
    yield service
    del user_repo


def test_login_service_with_correct_values_should_login_user(
    service: LoginService,
) -> None:
    assert isinstance(service.login(email="test@email.com", password="test_1234"), User)


def test_login_service_with_incorrect_password_should_raise_error(
    service: LoginService,
) -> None:
    with pytest.raises(CredentialsError):
        service.login(email="test@email.com", password="123")
