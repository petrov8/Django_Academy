# Generated by Django 4.1.3 on 2022-12-12 21:53

import django.core.validators
from django.db import migrations, models
import support.mixins.mixins
import support.validators.names


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="CourseModel",
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
                    "created",
                    models.DateField(
                        auto_created=True, null=True, verbose_name="Published"
                    ),
                ),
                (
                    "title",
                    models.CharField(
                        max_length=30,
                        unique=True,
                        validators=[
                            support.validators.names.check_if_letters_and_digits_only
                        ],
                        verbose_name="Title",
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        validators=[
                            support.validators.names.check_if_letters_and_digits_only
                        ],
                        verbose_name="Description",
                    ),
                ),
                (
                    "technology",
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
                        max_length=30,
                        verbose_name="Programming Language",
                    ),
                ),
                (
                    "participants",
                    models.PositiveIntegerField(
                        default=0, verbose_name="Total Participants"
                    ),
                ),
                (
                    "dev_type",
                    models.CharField(
                        choices=[
                            ("Front End", "Front End"),
                            ("Back End", "Back End"),
                            ("Full Stack", "Full Stack"),
                        ],
                        max_length=30,
                        verbose_name="Expertise",
                    ),
                ),
                (
                    "price",
                    models.FloatField(
                        validators=[
                            django.core.validators.MinValueValidator(
                                0, message="Price cannot be negative"
                            ),
                            django.core.validators.MaxValueValidator(
                                500, message="Price cannot exceed 500"
                            ),
                        ]
                    ),
                ),
                (
                    "image_url",
                    models.URLField(max_length=2048, verbose_name="Course Image"),
                ),
                (
                    "competency_level",
                    models.CharField(
                        choices=[
                            ("Beginner", "Beginner"),
                            ("Intermediate", "Intermediate"),
                            ("Advanced", "Advanced"),
                        ],
                        max_length=30,
                    ),
                ),
                ("start_date", models.DateField()),
                (
                    "modified",
                    models.DateField(
                        auto_now=True, null=True, verbose_name="Last Revision"
                    ),
                ),
            ],
            options={
                "verbose_name": "Course",
                "db_table": "4. Course",
                "ordering": ("-technology",),
            },
            bases=(support.mixins.mixins.SaveMixin, models.Model),
        ),
    ]
