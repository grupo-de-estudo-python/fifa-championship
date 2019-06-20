import pytest
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APIClient

from apps.championship.models import Championship

pytestmark = pytest.mark.django_db


def test_championship_list():
    api_client = APIClient()
    championship = Championship.objects.create(
        name="Campeonato", start_date="2019-06-20", end_date="2019-06-21"
    )

    response = api_client.get(reverse("championship-list"))

    assert response.status_code == status.HTTP_200_OK
    response_data = response.data[0]

    assert response_data["name"] == championship.name


def test_championship_post():
    api_client = APIClient()
    payload = {"name": "Campeonato", "start_date": "2019-06-20", "end_date": "2019-06-21"}
    response = api_client.post(reverse("championship-list"), data=payload)

    assert response.status_code == status.HTTP_201_CREATED

    championship = Championship.objects.first()

    assert championship.name == payload["name"]


def test_championship_update():
    api_client = APIClient()
    championship = Championship.objects.create(
        name="Campeonato", start_date="2019-06-20", end_date="2019-06-21"
    )

    payload = {"name": "Campeonato Dois"}
    response = api_client.patch(reverse("championship-detail", kwargs={"pk": championship.id}), data=payload)

    assert response.status_code == status.HTTP_200_OK
    championship.refresh_from_db()

    assert championship.name == payload["name"]
