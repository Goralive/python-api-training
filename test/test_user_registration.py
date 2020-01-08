from src.services import UserApiService


def test_can_registrate_user_with_valid_creds(faker):
    user = {"username": faker.name(), "password": "12345",
            "email": "demo@gmail.com"}
    response = UserApiService().create_user(user)

    assert response.status_code(200)
    assert len(response.field('id')) > 0


def test_cant_registrate_the_same_user(faker):
    user = {"username": faker.name(), "password": "12345",
            "email": "demo@gmail.com"}

    response = UserApiService().create_user(user)

    assert response.status_code(200)

    response = UserApiService().create_user(user)

    assert response.status_code(500)
