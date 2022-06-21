from faker import Faker

from .find_user_controller import FindUserController
from src.data.test import FindUserSpy
from src.infra.test import UserRepositorySpy
from src.presenters.helpers import HttpRequest


faker = Faker()


def test_handler_with_user_id_and_name():
    """Testing handle method"""
    find_user_use_case = FindUserSpy(UserRepositorySpy)
    find_user_controller = FindUserController(find_user_use_case)
    http_request = HttpRequest(
        query={"user_id": faker.random_number(), "user_name": faker.name()}
    )

    response = find_user_controller.handle(http_request)

    # Testing Inputs
    assert (
        find_user_use_case.by_id_and_name_param["user_id"]
        == http_request.query["user_id"]
    )
    assert (
        find_user_use_case.by_id_and_name_param["name"]
        == http_request.query["user_name"]
    )

    # Testing Outputs
    assert response.status_code == 200
    assert response.body


def test_handler_with_user_id():
    """Testing handle method"""
    find_user_use_case = FindUserSpy(UserRepositorySpy)
    find_user_controller = FindUserController(find_user_use_case)
    http_request = HttpRequest(query={"user_id": faker.random_number()})

    response = find_user_controller.handle(http_request)

    # Testing Inputs
    assert find_user_use_case.by_id_param["user_id"] == http_request.query["user_id"]
    assert find_user_use_case.by_name_param == {}
    assert find_user_use_case.by_id_and_name_param == {}

    # Testing Outputs
    assert response.status_code == 200
    assert response.body


def test_handler_with_name():
    """Testing handle method"""
    find_user_use_case = FindUserSpy(UserRepositorySpy)
    find_user_controller = FindUserController(find_user_use_case)
    http_request = HttpRequest(query={"user_name": faker.name()})

    response = find_user_controller.handle(http_request)

    # Testing Inputs
    assert find_user_use_case.by_name_param["name"] == http_request.query["user_name"]
    assert find_user_use_case.by_id_param == {}
    assert find_user_use_case.by_id_and_name_param == {}

    # Testing Outputs
    assert response.status_code == 200
    assert response.body


def test_handler_no_query_param():
    """Testing handle method"""
    find_user_use_case = FindUserSpy(UserRepositorySpy)
    find_user_controller = FindUserController(find_user_use_case)
    http_request = HttpRequest()

    response = find_user_controller.handle(http_request)

    # Testing Inputs
    assert find_user_use_case.by_id_and_name_param == {}
    assert find_user_use_case.by_id_param == {}
    assert find_user_use_case.by_name_param == {}

    # Testing Outputs
    assert response.status_code == 400
    assert "error" in response.body
