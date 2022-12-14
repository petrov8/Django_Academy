from django.contrib import admin
from django.contrib.admin import ModelAdmin

from app_payment.forms import CCPaymentForm
from app_payment.models import PaymentModel


# Register your models here.
@admin.register(PaymentModel)
class PaymentAdmin(ModelAdmin):
    list_display = ["cc_holder_first_name", "cc_holder_last_name", "course", "student"]
    add_form = CCPaymentForm