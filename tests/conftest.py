import pytest
from rest_framework.test import APIClient


@pytest.fixture()
def user(django_user_model):
    user_credentials = {
        'username': 'test_user',
        'password': 'test_password',
    }
    return django_user_model.objects.create_user(**user_credentials)


@pytest.fixture()
def api_client():
    return APIClient()


@pytest.fixture()
def auth_api_client(user):
    auth_api_client = APIClient()
    auth_api_client.force_authenticate(user=user)
    return auth_api_client
