# deals/tests/tests_models.py
from django.test import TestCase
from skills.models import ResourceLibrary


class ResourceLibraryTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.resource = ResourceLibrary.objects.create(
            type = 'course',
            description = 'Тестовый текст',
            learning_time = 20,
            url = '1.ru'
        )

    def test_verbose_name(self):
        """verbose_name в полях совпадает с ожидаемым."""
        
        resource = ResourceLibraryTest.resource
        field_verboses = {
            'type': 'Тип',
            'description': 'Описание',
            'learning_time': 'Время изучения',
            'url': 'Ссылка',
        }
        for field, expected_value in field_verboses.items():
            with self.subTest(field=field):
                self.assertEqual(
                    resource._meta.get_field(field).verbose_name, expected_value)


    def test_str(self):
        """Результат __str__ совпадает с ожидаемым."""

        resource = ResourceLibraryTest.resource
        self.assertEqual(str(resource), 'course')