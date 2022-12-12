from django.test import TestCase

from app_lecturer.forms import LecturerEditForm
from app_payment.forms import CCPaymentForm
from app_user.forms import UserRegisterForm, UserLoginForm, UserEditForm
from app_course.forms import CourseCreateForm


class BaseTestForm(TestCase):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.email = "doncho@abv.bg"
        self.password_1 = "SoftUni2022"
        self.password_2 = "SoftUni2022"

        self.credit_card_details = {
            "card_number": int("0001_0001_0001_0001"),
            "cc_holder_first_name": "Test",
            "cc_holder_last_name": "Testing",
            "cc_number": 393,
            "cc_expiry": "02/23"
        }

    @staticmethod
    def create_register_form(form_data):
        return UserRegisterForm(form_data)

    @staticmethod
    def create_login_form(form_data):
        return UserLoginForm(form_data)

    @staticmethod
    def create_course_form(form_data):
        return CourseCreateForm(form_data)

    @staticmethod
    def edit_user_form(form_data):
        return UserEditForm(form_data)

    @staticmethod
    def edit_lecturer_form(form_data):
        return LecturerEditForm(form_data)

    @staticmethod
    def create_credit_card_form(form_data):
        return CCPaymentForm(form_data)



