from django.contrib.auth import get_user_model

#<-----do not optimize file imports --- will delete ----->
from django.urls import reverse
from django.core.exceptions import ValidationError
from django.db import IntegrityError

from app_lecturer.models import LecturerModel
#<-----do not optimize file imports --- will delete ----->

from app_user.models import UserProfileModel
from django_academy.tests.base import BaseTestClass


UserModel = get_user_model()

sample_profile_pic = "https://cdn.pixabay.com/photo/2016/12/14/03/08/raccoon-1905528__340.jpg"


class BaseTestUser(BaseTestClass):

    def setUp(self):
        self.credentials = {
            "email": "doncho_e_pich@abv.bg",
            "password": "SoftUni2022"
        }

        self.profile_details = {
            "first_name": "Test",
            "last_name": "Testing",
            "age": 20,
            "gender": "Male",
            "profile_picture": sample_profile_pic
        }

        self.test_user = UserModel.objects.create_user(**self.credentials)
        self.client.login(**self.credentials)

    def create_test_user(self):
        return UserModel.objects.create_user(**self.credentials)

    def user_exists(self):
        try:
            return UserModel.objects.filter(id=self.test_user.id)[0]
        except IndexError:
            return False

    def profile_exists(self):
        try:
            return UserProfileModel.objects.filter(user_id=self.test_user.id)[0]
        except IndexError:
            return False

    def lecturer_exists(self):
        try:
            return LecturerModel.objects.filter(user_id=self.test_user.id)[0]
        except IndexError:
            return False

    def change_user_role_to_lecturer(self):
        self.test_user.role = "Lecturer"
        self.test_user.user_permissions.add(33)
        self.test_user.user_permissions.add(34)
        self.test_user.user_permissions.add(35)
        self.test_user.save()
        self.client.logout()

        self.client.login(**self.credentials)
        if self.test_user.groups.filter(name="Lecturer").exists():
            return self.test_user

    def change_user_role_to_admin(self):
        self.test_user.role = "Admin"
        self.test_user.user_permissions.add(22)
        self.test_user.user_permissions.add(23)
        self.test_user.save()
        self.client.logout()

        self.client.login(**self.credentials)
        if self.test_user.groups.filter(name="Admin").exists():
            return self.test_user






