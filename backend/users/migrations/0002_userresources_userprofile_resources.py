# Generated by Django 4.2.7 on 2023-12-01 11:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("skills", "0002_skill_level"),
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="UserResources",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[("done", "Изучен"), ("process", "В процессе")],
                        max_length=8,
                    ),
                ),
                (
                    "profile",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="resourse_user",
                        to="users.userprofile",
                        verbose_name="Пользователь",
                    ),
                ),
                (
                    "resource",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="resource_user",
                        to="skills.resourcelibrary",
                        verbose_name="Ресурс",
                    ),
                ),
            ],
            options={
                "verbose_name": "Ресурс пользователя",
                "verbose_name_plural": "Ресурсы пользователя",
            },
        ),
        migrations.AddField(
            model_name="userprofile",
            name="resources",
            field=models.ManyToManyField(
                related_name="user_recources",
                through="users.UserResources",
                to="skills.resourcelibrary",
                verbose_name="Изученные ресурсы",
            ),
        ),
    ]
