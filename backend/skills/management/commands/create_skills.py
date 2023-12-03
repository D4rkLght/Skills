from skills.factories import create_skills
from skills.utils.db_command import CommandCreateObjects as BaseCommand


class Command(BaseCommand):
    """Создание тестовых ресурсов."""

    def _generate(self, amount: int):
        create_skills(amount)
