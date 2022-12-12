# Generated by Django 4.1.3 on 2022-11-28 14:35

import creditcards.models
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import support.validators.names
import support.validators.payment


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("app_course", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="PaymentModel",
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
                    "cc_holder_first_name",
                    models.CharField(
                        max_length=30,
                        validators=[
                            support.validators.names.check_if_letters_only,
                            django.core.validators.MinLengthValidator(
                                2, message="Name must be longer than 2 characters."
                            ),
                        ],
                        verbose_name="First Name",
                    ),
                ),
                (
                    "cc_holder_last_name",
                    models.CharField(
                        max_length=30,
                        validators=[
                            support.validators.names.check_if_letters_only,
                            django.core.validators.MinLengthValidator(
                                2, message="Name must be longer than 2 characters."
                            ),
                        ],
                        verbose_name="Last Name",
                    ),
                ),
                (
                    "cc_number",
                    creditcards.models.CardNumberField(
                        max_length=25,
                        validators=[support.validators.payment.check_card_number],
                        verbose_name="card number",
                    ),
                ),
                (
                    "cc_expiry",
                    creditcards.models.CardExpiryField(verbose_name="expiration date"),
                ),
                (
                    "cc_code",
                    creditcards.models.SecurityCodeField(
                        max_length=4, verbose_name="security code"
                    ),
                ),
                (
                    "course",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="app_course.coursemodel",
                    ),
                ),
            ],
            options={
                "verbose_name": "Payment",
                "db_table": "5. Payment",
                "ordering": ("-cc_holder_first_name",),
            },
        ),
    ]
