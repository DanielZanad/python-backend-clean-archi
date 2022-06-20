from faker import Faker
from .find import FindUser
from src.infra.test import UserRepositorySpy

faker = Faker()


def test_by_id():
    """Testing by_id"""
    user_repo = UserRepositorySpy()
    find_user = FindUser(user_repo)

    attributes = {"id": faker.random_number(digits=2)}
    response = find_user.by_id(user_id=attributes["id"])

    # Testing Inputs
    assert user_repo.select_user_params["user_id"] == attributes["id"]

    # Testing Outputs
    assert response["Success"] is True
    assert response["Data"]


def test_by_name():
    """Testing by_name"""
    user_repo = UserRepositorySpy()
    find_user = FindUser(user_repo)

    attributes = {"name": faker.name()}
    response = find_user.by_name(name=attributes["name"])

    # Testing Inputs
    assert user_repo.select_user_params["name"] == attributes["name"]

    # Testing Outputs
    assert response["Success"] is True
    assert response["Data"]


def test_by_id_and_name():
    """Testing by_id_name"""
    user_repo = UserRepositorySpy()
    find_user = FindUser(user_repo)

    attributes = {"id": faker.random_number(digits=2), "name": faker.name()}
    response = find_user.by_id_and_name(
        user_id=attributes["id"], name=attributes["name"]
    )

    print(response)

    # Testing Inputs
    assert user_repo.select_user_params["user_id"] == attributes["id"]
    assert user_repo.select_user_params["name"] == attributes["name"]

    # Testing Outputs
    assert response["Success"] is True
    assert response["Data"]
