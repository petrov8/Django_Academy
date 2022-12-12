from django_academy.tests.forms.base_form import BaseTestForm


class RegisterForm(BaseTestForm):

    def __int__(self, email, password_1, password_2):
        super().__init__(email, password_1, password_2)

    def setUp(self):
        self.form_data = {
            "email": self.email,
            "password1": self.password_1,
            "password2": self.password_2,
        }

    def test_register__new_user__with_valid_data(self):
        form = super().create_register_form(self.form_data)

        self.assertTrue(form.is_valid())

    def test_register__new_user__with_invalid_email(self):
        self.form_data["email"] = "invalid"
        form = super().create_register_form(self.form_data)

        self.assertFalse(form.is_valid())

    def test_register__new_user__with_missing_email(self):
        self.form_data["email"] = ""
        form = super().create_register_form(self.form_data)

        self.assertFalse(form.is_valid())

    def test_register__new_user__with_missing_password_1(self):
        self.form_data["password1"] = ""
        form = super().create_register_form(self.form_data)

        self.assertFalse(form.is_valid())

    def test_register__new_user__with_different_passwords(self):
        self.form_data["password1"] = "different"

        form = super().create_register_form(self.form_data)

        self.assertFalse(form.is_valid())

    def test_register__new_user__with_empty_fields(self):
        for field in self.form_data.keys():
            self.form_data[field] = ""

        form = super().create_register_form(self.form_data)

        self.assertFalse(form.is_valid())

