import requests
import pytest
from assertpy import assert_that

@pytest.fixture()
def base_url():
    return "https://reqres.in/api"

def test_get_user_not_found(base_url):
    response = requests.get(f'{base_url}/users/23')
    assert response.status_code == 404
    assert response.reason == "Not Found"

def test_login(base_url):
    credentials = {"email": "eve.holt@reqres.in", "password": "cityslicka"}
    request = requests.post(f'{base_url}/login', json=credentials)
    response = request.json()
    assert request.status_code == 200
    assert_that(response).contains('token')
    assert response['token'] == 'QpwL5tke4Pnpja7X4'


