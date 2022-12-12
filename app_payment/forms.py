from app_payment.models import PaymentModel
from support.base.base_forms import BaseModelForm


class CCPaymentForm(BaseModelForm):
    class Meta:
        model = PaymentModel
        fields = (
            "cc_number",
            "cc_expiry",
            "cc_code",
            "cc_holder_first_name",
            "cc_holder_last_name",
        )


