import random

import pytest


@pytest.fixture(autouse=True)
def seeder() -> None:
    random.seed(42)
