# Generated by Django 4.1.3 on 2022-11-28 14:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import support.mixins.mixins


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("app_user", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="LecturerModel",
            fields=[
                ("created", models.DateTimeField(auto_created=True)),
                (
                    "years_of_experience",
                    models.PositiveIntegerField(
                        blank=True, null=True, verbose_name="Years of Experience"
                    ),
                ),
                (
                    "fav_language",
                    models.CharField(
                        choices=[
                            ("C++", "C++"),
                            ("C#", "C#"),
                            ("Java", "Java"),
                            ("JS", "JS"),
                            ("TS", "TS"),
                            ("Python", "Python"),
                            ("Cobalt", "Cobalt"),
                            ("PHP", "PHP"),
                            ("GO", "GO"),
                            ("Swift", "Swift"),
                            ("Kotlin", "Kotlin"),
                            ("Objective C", "Objective C"),
                            ("R", "R"),
                            ("Matlab", "Matlab"),
                        ],
                        default="Select",
                        max_length=30,
                        verbose_name="Favourite Language",
                    ),
                ),
                ("about_me", models.TextField(verbose_name="About")),
                ("modified", models.DateTimeField(auto_now=True)),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        primary_key=True,
                        serialize=False,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                ("is_completed", models.BooleanField(default=False)),
            ],
            options={
                "verbose_name": "Lecturer Profile",
                "db_table": "3. LecturerProfile",
                "ordering": ("-created",),
            },
            bases=(support.mixins.mixins.SaveMixin, models.Model),
        ),
    ]
