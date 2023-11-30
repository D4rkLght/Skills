from http import HTTPStatus

from django.urls import reverse

from tests.fixtures import BaseCaseForSkillsTests


class SkillsViewTests(BaseCaseForSkillsTests):
    """
    Test class for candidate Views
    """

    def test_check_view(self):
        """
        Test check view
        """

        for endpoint in self.ENDPOINTS:
            with self.subTest(endpoint):
                response = self.client.get(endpoint)
                self.assertEqual(response.status_code, HTTPStatus.UNAUTHORIZED)

        for endpoint in self.ENDPOINTS:
            with self.subTest(endpoint=endpoint):
                response = self.auth_client.get(endpoint)
                self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_check_registration_view(self):
        """
        Test for check registration
        """
        response = self.client.post(
            reverse("api:v1:users-list"),
            {
                "trecker_id": "trecker",
                "email": "user@example1.com",
                "username": "user1",
                "password": "sfafs23efdssa",
            },
        )
        self.assertEqual(response.status_code, HTTPStatus.CREATED)
