from hamcrest import greater_than, has_length

from src.conditions import body, status_code
from src.services import UserApiService


def test_can_registrate_user_with_valid_creds(faker):
    user = {"username": faker.name(), "password": "12345",
            "email": "demo@gmail.com"}
    response = UserApiService().create_user(user)

    response.should_have(status_code(200))
    response.should_have(body("$.id", has_length(greater_than(0))))


def test_cant_registrate_the_same_user(faker):
    user = {"username": faker.name(), "password": "12345",
            "email": "demo@gmail.com"}

    response = UserApiService().create_user(user)

    response.should_have(status_code(200))

    response = UserApiService().create_user(user)

    response.should_have(status_code(500))
