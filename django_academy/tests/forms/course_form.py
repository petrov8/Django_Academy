from django_academy.tests.forms.base_form import BaseTestForm

sample_image_url = "https://www.freecodecamp.org/news/content/images/2022/02/Banner-10.png"


class CreateCourseForm(BaseTestForm):

    def setUp(self):
        self.form_data = {
            "title": "Test",
            "description": "Testing purposes",
            "technology": "Python",
            "dev_type": "Front End",
            "competency_level": "Beginner",
            "price": 450,
            "image_url": sample_image_url,
            "start_date": "25 Dec 2022"
        }

        self.max_field_chars = 30

    def test_form__create_course__with_valid_data(self):

        form = super().create_course_form(self.form_data)
        print(form.errors)
        self.assertTrue(form.is_valid())

    def test_max_field__title__with_invalid_len(self):
        self.form_data["title"] = "A" * (self.max_field_chars + 1 )
        form = super().create_course_form(self.form_data)
        self.assertFalse(form.is_valid())

    def test_max_field__title__with_valid_len(self):
        self.form_data["title"] = "A" * self.max_field_chars
        form = super().create_course_form(self.form_data)
        self.assertTrue(form.is_valid())

    def test_min_price__price__with_negative(self):
        self.form_data["price"] = -1
        form = super().create_course_form(self.form_data)
        self.assertFalse(form.is_valid())

    def test_min_price__price__with_zero(self):
        self.form_data["price"] = 0
        form = super().create_course_form(self.form_data)
        self.assertTrue(form.is_valid())

    def test_enums__technology__with_invalid_entry(self):
        self.form_data["technology"] = "some stack"
        form = super().create_course_form(self.form_data)
        self.assertFalse(form.is_valid())

    def test_enums__dev_type__with_invalid_entry(self):
        self.form_data["dev_type"] = "some stack"
        form = super().create_course_form(self.form_data)
        self.assertFalse(form.is_valid())

    def test_url__image_url__with_invalid_entry(self):
        self.form_data["image_url"] = "some stack"
        form = super().create_course_form(self.form_data)
        self.assertFalse(form.is_valid())

    def test_url_len__image_url__with_invalid_len(self):
        self.form_data["image_url"] = "a" * 2049
        form = super().create_course_form(self.form_data)
        self.assertFalse(form.is_valid())

    def test_url_len__image_url__with_valid_max_len(self):
        self.form_data["image_url"] = "a" * 2048
        form = super().create_course_form(self.form_data)
        self.assertFalse(form.is_valid())

    def test_enums__competency_level__with_invalid_entry(self):
        self.form_data["competency_level"] = "some stack"
        form = super().create_course_form(self.form_data)
        self.assertFalse(form.is_valid())