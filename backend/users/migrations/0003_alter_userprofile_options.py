# Generated by Django 4.2.7 on 2023-12-10 08:38

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0002_alter_userskill_skill"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="userprofile",
            options={
                "ordering": ("id",),
                "verbose_name": "Данные пользователя",
                "verbose_name_plural": "Данные пользователя",
            },
        ),
    ]