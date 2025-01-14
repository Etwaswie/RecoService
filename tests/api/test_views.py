from http import HTTPStatus

from starlette.testclient import TestClient

from service.api.authorization import APIKeys
from service.settings import ServiceConfig

GET_RECO_PATH = "/reco/{model_name}/{user_id}"
models = ["top_20_popular"]


def test_health(
    client: TestClient,
) -> None:
    with client:
        response = client.get("/health")
    assert response.status_code == HTTPStatus.OK


def test_get_reco_success(
    client: TestClient,
    service_config: ServiceConfig,
) -> None:
    user_id = 123
    for model_name in models:
        path = GET_RECO_PATH.format(model_name=model_name, user_id=user_id)
        with client:
            response = client.get(path, headers={"Authorization": APIKeys})
        assert response.status_code == HTTPStatus.OK
        response_json = response.json()
        assert response_json["user_id"] == user_id
        assert len(response_json["items"]) == 10
        assert all(isinstance(item_id, int) for item_id in response_json["items"])


def test_get_reco_for_unknown_user(
    client: TestClient,
) -> None:
    user_id = 10**10
    model_name = "random"
    path = GET_RECO_PATH.format(model_name=model_name, user_id=user_id)
    with client:
        response = client.get(path, headers={"Authorization": APIKeys})
    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json()["errors"][0]["error_key"] == "user_not_found"


def test_get_reco_for_unknown_model(
    client: TestClient,
) -> None:
    user_id = 123
    model_name = "error_model"
    path = GET_RECO_PATH.format(model_name=model_name, user_id=user_id)
    with client:
        response = client.get(path, headers={"Authorization": APIKeys})
    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json()["errors"][0]["error_key"] == "model_not_found"


def failed_authorization(
    client: TestClient,
) -> None:
    user_id = 123
    model_name = "top"
    path = GET_RECO_PATH.format(model_name=model_name, user_id=user_id)
    with client:
        response = client.get(path, headers={"Authorization": "FailAPI"})
    assert response.status_code == HTTPStatus.UNAUTHORIZED
    assert response.json()["errors"][0]["error_key"] == "user_not_authorized"
