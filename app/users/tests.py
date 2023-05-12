from django.test import Client, TestCase

from users.models import AccessRequest


TEST_NAME = "TEST_NAME"
TEST_ORGANIZATION = "TEST_ORGANIZATION"
TEST_INTEREST = "TEST_INTEREST"
TEST_USE_CASE = "TEST_USE_CASE"
TEST_HUMANS_DAILY = 3


class AccessRequestTestCase(TestCase):
    def test_access_request(self):
        """Animals that can speak are correctly identified"""

        client = Client()
        response = client.post(
            "/access_request",
            {
                "name": TEST_NAME,
                "organization": TEST_ORGANIZATION,
                "interest": TEST_INTEREST,
                "use_case": TEST_USE_CASE,
                "humans_daily": TEST_HUMANS_DAILY,
            },
        )
        assert response.status_code == 200
        assert AccessRequest.objects.count() > 0
