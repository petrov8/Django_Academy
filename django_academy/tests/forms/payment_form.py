from django_academy.tests.forms.base_form import BaseTestForm


class CreatePaymentForm(BaseTestForm):

    def test_form__cc_payment__with_correct_details(self):
        form = super().create_credit_card_form(self.credit_card_details)
        self.assertTrue(form.is_valid())





