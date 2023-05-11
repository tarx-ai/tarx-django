import pytest

from django.test import Client

# from .models import Application


TEST_NAME = "TEST_NAME"
TEST_ORGANIZATION = "TEST_ORGANIZATION"
TEST_INTEREST = "TEST_INTEREST"
TEST_USE_CASE = "TEST_USE_CASE"
TEST_HUMANS_DAILY = 3


@pytest.mark.django_db
def test_application():
    client = Client()
    response = client.post(
        "/register",
        {
            "name": TEST_NAME,
            "organization": TEST_ORGANIZATION,
            "interest": TEST_INTEREST,
            "use_case": TEST_USE_CASE,
            "humans_daily": TEST_HUMANS_DAILY,
        },
    )
    assert response.status_code == 200
