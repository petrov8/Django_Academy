from django_academy.tests.forms.base_form import BaseTestForm


class LecturerProfileForm(BaseTestForm):

    def setUp(self):
        self.form_data = {
            "years_of_experience": 17,
            "fav_language": "Python",
            "about_me": "A cool dude",
        }
        self.max_field_chars = 30

    def test_form__edit_lecturer__with_valid_data(self):
        form = super().edit_lecturer_form(self.form_data)
        self.assertTrue(form.is_valid())

    def test_min_chars_first_and_last_names__edit_user__valid_input(self):
        self.form_data["first_name"] = "aa"
        self.form_data["last_name"] = "aa"

        form = super().edit_lecturer_form(self.form_data)
        self.assertTrue(form.is_valid())

    def test_age_gender_picture__edit_user__invalid_input_type(self):
        tested_fields = ["age", "gender", "profile_picture"]
        for key in self.form_data.keys():
            if key in tested_fields:
                field_value = self.form_data[key]
                self.form_data[key] = "invalid"
                form = super().edit_lecturer_form(self.form_data)
                self.assertFalse(form.is_valid())
                self.form_data[key] = field_value

    def test_age__edit_user__wrong_input_type(self):
        self.form_data["age"] = "hello"

        form = super().edit_lecturer_form(self.form_data)
        self.assertTrue(form.is_valid())

    def test_experience__edit_user__below_zero(self):
        self.form_data["years_of_experience"] = -1

        form = super().edit_lecturer_form(self.form_data)
        self.assertFalse(form.is_valid())

    def test_experience__edit_user__valid_input(self):
        self.form_data["years_of_experience"] = 1

        form = super().edit_lecturer_form(self.form_data)
        self.assertTrue(form.is_valid())

