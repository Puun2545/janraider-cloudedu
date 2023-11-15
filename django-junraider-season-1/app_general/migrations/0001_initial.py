# Generated by Django 4.0 on 2021-12-10 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Subscription",
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
                ("name", models.CharField(max_length=50)),
                ("email", models.EmailField(max_length=50, unique=True)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("unapproved", "Unapproved"),
                            ("banned", "Banned"),
                            ("approved", "Approved"),
                        ],
                        default="unapproved",
                        max_length=15,
                    ),
                ),
                ("registeredAt", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]