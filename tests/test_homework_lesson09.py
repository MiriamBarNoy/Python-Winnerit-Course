import requests
import pytest
from assertpy import assert_that
import csv

@pytest.fixture()
def base_url():
    return "https://jsonplaceholder.typicode.com"


def test_get_users_sanity(base_url):
    response = requests.get(f'{base_url}/users/')
    expected_keys = {"id","name", "username", "email", "address", "phone", "website", "company"}
    assert response.status_code == 200
    assert_that(response.json()).is_length(10)
    assert_that(response.json())._dict_include(expected_keys)

def test_user_not_found(base_url):
    response = requests.get(f'{base_url}/users/11')
    assert response.status_code == 404
    assert_that(response.reason).is_equal_to("Not Found")

users_data = [
              (0, 'name', 'Leanne Graham'),
              (1, 'username', 'Antonette'),
              (3,'email','Julianne.OConner@kory.org'),
              (4,'address.street','Skiles Walks')
             ]
# def get_test_data_from_csv():
#     with open('test_data.csv', newline='') as csvfile:
#         reader = csv.DictReader(csvfile)
#         next(reader)  # Skip the header row
#         return [(row[0], str(row[1]), str(row[2])) for row in reader]

@pytest.mark.parametrize("entry,field,value",users_data)
def test_users(entry,field,value, base_url):
    response = requests.get(f'{base_url}/users')
    json_data = response.json()
    actual_value = json_data[int(entry)]
    for key in field.split('.'):
        actual_value = actual_value[key]

    assert actual_value == value





