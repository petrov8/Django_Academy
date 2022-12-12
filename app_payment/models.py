from django.core.validators import MinLengthValidator
from django.db import models

from creditcards.models import CardNumberField, CardExpiryField, SecurityCodeField

from app_course.models import CourseModel
from app_user.models import UserBaseModel
from support.validators import names, payment


class PaymentModel(models.Model):
    MIN_DEFAULT_FIELD_LEN = 2
    MAX_DEFAULT_FIELD_LEN = 30

    class Meta:
        ordering = ("-cc_holder_first_name",)
        db_table = "5. Payment"
        verbose_name = "Payment"

    cc_holder_first_name = models.CharField(
        verbose_name="First Name",
        blank=False,
        null=False,
        validators=[
            names.check_if_letters_only,
            MinLengthValidator(MIN_DEFAULT_FIELD_LEN, message="Name must be longer than 2 characters.")
        ],
        max_length=MAX_DEFAULT_FIELD_LEN,
    )

    cc_holder_last_name = models.CharField(
        verbose_name="Last Name",
        blank=False,
        null=False,
        validators=[
            names.check_if_letters_only,
            MinLengthValidator(MIN_DEFAULT_FIELD_LEN, message="Name must be longer than 2 characters.")
        ],
        max_length=MAX_DEFAULT_FIELD_LEN,
    )

    cc_number = CardNumberField('card number', validators=[payment.check_card_number])
    cc_expiry = CardExpiryField('expiration date')
    cc_code = SecurityCodeField('security code')

    course = models.ForeignKey(
        CourseModel,
        null=True,
        on_delete=models.CASCADE,
        primary_key=False
    )

    student = models.ForeignKey(
        UserBaseModel,
        null=True,
        on_delete=models.CASCADE,
        primary_key=False,
    )










