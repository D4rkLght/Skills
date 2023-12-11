from django.test import TestCase, Client


class AuthorizeTests(TestCase):
    """доступ неавторизованных пользователей."""

    def setUp(self):
        self.guest_client = Client()


    def test_about_url_exists_at_desired_location(self):
        """Проверка доступности адреса /api/v1/skills/."""
        response = self.guest_client.get('/api/v1/skills/')
        self.assertEqual(response.status_code, 401)