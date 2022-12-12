from django.contrib.auth import get_user_model
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from app_user.enums import UserGenderEnum, UserRoleEnum
from app_user.user_manager import CustomBaseUserManager
from support.mixins.mixins import SaveMixin
from support.validators.names import check_if_letters_only

MAX_DEFAULT_FIELD_LEN = 30


class UserBaseModel(AbstractBaseUser, PermissionsMixin):
    ordering = ("email",)

    class Meta:
        db_table = "1. User"
        verbose_name = "User"

    email = models.EmailField(
        verbose_name="Email",
        unique=True,
        max_length=MAX_DEFAULT_FIELD_LEN
    )

    role = models.CharField(
        verbose_name="Category",
        choices=[(role.value, role.value) for role in UserRoleEnum],
        default="Student",
        max_length=MAX_DEFAULT_FIELD_LEN
    )

    is_staff = models.BooleanField(
        default=False
    )

    is_superuser = models.BooleanField(
        default=False
    )

    USERNAME_FIELD = "email"

    objects = CustomBaseUserManager()

    def __str__(self):
        return self.email


class UserProfileModel(SaveMixin, models.Model):
    class Meta:
        ordering = ("-created", )
        db_table = "2. UserProfile"
        verbose_name = "User Profile"

    MIN_NAME_LEN = 2

    first_name = models.CharField(
        verbose_name="First Name",
        blank=True,
        null=True,
        validators=[
            MinLengthValidator(MIN_NAME_LEN, message="Name must have at least 2 chars."),
            check_if_letters_only
        ],
        max_length=MAX_DEFAULT_FIELD_LEN
    )

    last_name = models.CharField(
        verbose_name="Last Name",
        blank=True,
        null=True,
        validators=[
            MinLengthValidator(MIN_NAME_LEN, message="Name must have at least 2 chars."),
            check_if_letters_only
        ],
        max_length=MAX_DEFAULT_FIELD_LEN
    )

    age = models.PositiveIntegerField(
        verbose_name="Age",
        blank=True,
        null=True,
        validators=[
            MinValueValidator(14, message="You must be at least 14 years of age"),
        ],

    )

    gender = models.CharField(
        verbose_name="Gender",
        choices=[(gender.value, gender.value) for gender in UserGenderEnum],
        default="Select",
        max_length=MAX_DEFAULT_FIELD_LEN
    )

    profile_picture = models.URLField(
        verbose_name="Profile Picture",
        blank=True,
        null=True
    )

    created = models.DateTimeField(
        editable=False,
    )

    modified = models.DateTimeField(
        null=True,
    )

    user = models.OneToOneField(
        get_user_model(),
        primary_key=True,
        on_delete=models.CASCADE
    )

    is_completed = models.BooleanField(
        default=False,
    )












