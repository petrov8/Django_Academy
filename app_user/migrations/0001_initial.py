# Generated by Django 4.1.3 on 2022-11-28 14:35

import app_user.user_manager
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import support.mixins.mixins
import support.validators.names


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="UserBaseModel",
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
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "email",
                    models.EmailField(max_length=30, unique=True, verbose_name="Email"),
                ),
                (
                    "role",
                    models.CharField(
                        choices=[
                            ("Student", "Student"),
                            ("Lecturer", "Lecturer"),
                            ("Admin", "Admin"),
                            ("Master", "Master"),
                        ],
                        default="Student",
                        max_length=30,
                        verbose_name="Category",
                    ),
                ),
                ("is_staff", models.BooleanField(default=False)),
                ("is_superuser", models.BooleanField(default=False)),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "verbose_name": "User",
                "db_table": "1. User",
            },
            managers=[
                ("objects", app_user.user_manager.CustomBaseUserManager()),
            ],
        ),
        migrations.CreateModel(
            name="UserProfileModel",
            fields=[
                (
                    "first_name",
                    models.CharField(
                        blank=True,
                        max_length=30,
                        null=True,
                        validators=[
                            django.core.validators.MinLengthValidator(
                                2, message="Name must have at least 2 chars."
                            ),
                            support.validators.names.check_if_letters_only,
                        ],
                        verbose_name="First Name",
                    ),
                ),
                (
                    "last_name",
                    models.CharField(
                        blank=True,
                        max_length=30,
                        null=True,
                        validators=[
                            django.core.validators.MinLengthValidator(
                                2, message="Name must have at least 2 chars."
                            ),
                            support.validators.names.check_if_letters_only,
                        ],
                        verbose_name="Last Name",
                    ),
                ),
                (
                    "age",
                    models.PositiveIntegerField(
                        blank=True, null=True, verbose_name="Age"
                    ),
                ),
                (
                    "gender",
                    models.CharField(
                        choices=[
                            ("Male", "Male"),
                            ("Female", "Female"),
                            ("Prefer not to say", "Prefer not to say"),
                        ],
                        default="Select",
                        max_length=30,
                        verbose_name="Gender",
                    ),
                ),
                (
                    "profile_picture",
                    models.URLField(
                        blank=True, null=True, verbose_name="Profile Picture"
                    ),
                ),
                ("created", models.DateTimeField(editable=False)),
                ("modified", models.DateTimeField(null=True)),
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
                "verbose_name": "User Profile",
                "db_table": "2. UserProfile",
                "ordering": ("-created",),
            },
            bases=(support.mixins.mixins.SaveMixin, models.Model),
        ),
    ]
