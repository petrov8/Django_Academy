from django.contrib.auth import get_user_model
from django.db import models

from app_lecturer.enums import ScriptingLangsEnum
from support.mixins.mixins import SaveMixin, AuditTrailMixin


class LecturerModel(SaveMixin,AuditTrailMixin,  models.Model):
    MAX_DEFAULT_FIELD_LEN = 30

    class Meta:
        ordering = ("-created", )
        db_table = "3. LecturerProfile"
        verbose_name = "Lecturer Profile"

    years_of_experience = models.PositiveIntegerField(
        verbose_name="Years of Experience",
        blank=True,
        null=True,
    )

    fav_language = models.CharField(
        verbose_name="Favourite Language",
        max_length=MAX_DEFAULT_FIELD_LEN,
        choices=[(lang.value, lang.value) for lang in ScriptingLangsEnum],
        default="Select",
    )

    about_me = models.TextField(
        verbose_name="About"
    )

    user = models.OneToOneField(
        get_user_model(),
        primary_key=True,
        on_delete=models.CASCADE
    )

    is_completed = models.BooleanField(
        default=False
    )

