import pytest
from django.urls import reverse
from rest_framework import status

pytestmark = pytest.mark.django_db


def test_no_auth(api_client):
    url = reverse('api:tests-list')

    response = api_client.get(url)

    assert response.status_code == status.HTTP_401_UNAUTHORIZED


def test_auth(auth_api_client):
    url = reverse('api:tests-list')

    response = auth_api_client.get(url)

    assert response.status_code == status.HTTP_200_OK
