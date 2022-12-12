
from django_academy.tests.forms.base_form import BaseTestForm

sample_image = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ_D_V-9nqKdCGs23bXMI9wSoZ6Bl3jeA-ZGYeZvp2BdcnzuRwf29G5ki9oIlP7Rt6X8FA&usqp=CAU"


class UserProfileForm(BaseTestForm):

    def setUp(self):
        self.form_data = {
            "first_name": "Test",
            "last_name": "Testing",
            "age": "18",
            "gender": "Male",
            "profile_picture": sample_image,

        }
        self.max_field_chars = 30
        self.max_char_fields = ["first_name", "last_name"]

    def test_form__edit_user__with_valid_data(self):
        form = super().edit_user_form(self.form_data)
        self.assertTrue(form.is_valid())

    def test_min_chars_first_and_last_names__edit_user__invalid_input(self):
        self.form_data["first_name"] = "a"
        self.form_data["last_name"] = "a"

        form = super().edit_user_form(self.form_data)
        self.assertFalse(form.is_valid())

    def test_min_chars_first_and_last_names__edit_user__valid_input(self):
        self.form_data["first_name"] = "aa"
        self.form_data["last_name"] = "aa"

        form = super().edit_user_form(self.form_data)
        self.assertTrue(form.is_valid())

    def test_age_gender_picture__edit_user__invalid_input_type(self):
        tested_fields = ["age", "gender", "profile_picture"]
        for key in self.form_data.keys():
            if key in tested_fields:
                field_value = self.form_data[key]
                self.form_data[key] = "invalid"
                form = super().edit_user_form(self.form_data)
                self.assertFalse(form.is_valid())
                self.form_data[key] = field_value

    def test_default_max_chars__edit_user__invalid_len(self):
        self.form_data["first_name"] = "a" * (self.max_field_chars + 1)
        self.form_data["last_name"] = "a" * (self.max_field_chars + 1)

        form = super().edit_user_form(self.form_data)
        self.assertFalse(form.is_valid())

    def test_default_max_chars__edit_user__valid_len(self):
        self.form_data["first_name"] = "a" * self.max_field_chars
        self.form_data["last_name"] = "a" * self.max_field_chars

        form = super().edit_user_form(self.form_data)
        self.assertTrue(form.is_valid())

    def test_age__edit_user__wrong_input_type(self):
        self.form_data["age"] = "hello"

        form = super().edit_user_form(self.form_data)
        self.assertFalse(form.is_valid())

    def test_age__edit_user__below_zero(self):
        self.form_data["age"] = "-1"

        form = super().edit_user_form(self.form_data)
        self.assertFalse(form.is_valid())

    def test_age__edit_user__valid_input(self):
        self.form_data["age"] = "1"

        form = super().edit_user_form(self.form_data)
        self.assertTrue(form.is_valid())
