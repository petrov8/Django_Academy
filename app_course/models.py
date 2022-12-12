from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from app_course.enums import DevTypeEnums, CompetencyEnums
from app_lecturer.enums import ScriptingLangsEnum
from app_lecturer.models import LecturerModel
from app_user.models import UserProfileModel
from support.mixins.mixins import SaveMixin
from support.validators.names import check_if_letters_and_digits_only

UserModel = get_user_model()


class CourseModel(SaveMixin, models.Model):
    MAX_DEFAULT_FIELD_LEN = 30
    MIN_RATING = 0
    MIN_PRICE = 0
    MAX_PRICE = 500

    class Meta:
        ordering = ("-technology", )
        db_table = "4. Course"
        verbose_name = "Course"

    title = models.CharField(
        verbose_name="Title",
        unique= True,
        blank=False,
        null=False,
        max_length=MAX_DEFAULT_FIELD_LEN,
        validators=[check_if_letters_and_digits_only]
    )

    description = models.TextField(
        verbose_name="Description",
        blank=False,
        null=False,
        validators=[check_if_letters_and_digits_only]
    )

    technology = models.CharField(
        verbose_name="Programming Language",
        blank=False,
        null=False,
        choices=[(lang.value, lang.value) for lang in ScriptingLangsEnum],
        max_length=MAX_DEFAULT_FIELD_LEN
    )

    participants = models.PositiveIntegerField(
        verbose_name="Total Participants",
        default=0
    )

    dev_type = models.CharField(
        verbose_name="Expertise",
        blank=False,
        null=False,
        choices=[(dev.value, dev.value) for dev in DevTypeEnums],
        max_length=MAX_DEFAULT_FIELD_LEN
    )

    price = models.FloatField(
        validators=[
            MinValueValidator(MIN_PRICE, message="Price cannot be negative"),
            MaxValueValidator(MAX_PRICE, message=f"Price cannot exceed {MAX_PRICE}")
        ]
    )

    image_url = models.URLField(
        verbose_name="Course Image",
        blank=False,
        null=False,
        max_length=2048,
    )

    competency_level = models.CharField(
        choices=[(level.value, level.value) for level in CompetencyEnums],
        max_length=MAX_DEFAULT_FIELD_LEN
    )

    start_date = models.DateField(

    )

    created = models.DateField(
        verbose_name="Published",
        auto_created=True,
        null=True,
    )

    modified = models.DateField(
        verbose_name="Last Revision",
        auto_now=True,
        null=True,
    )

    creator = models.ForeignKey(
        LecturerModel,
        primary_key=False,
        on_delete=models.CASCADE
    )

    students = models.ManyToManyField(
        UserModel,
        primary_key=False,
    )

















