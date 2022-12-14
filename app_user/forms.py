from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from app_user.models import UserProfileModel, UserBaseModel
from support.base.base_forms import BaseModelForm, BaseGenericForm

UserModel = get_user_model()


class BaseAuthForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(BaseAuthForm, self).__init__(*args, **kwargs)
        self.__hide_help_text()

    def __hide_help_text(self):
        for field_name in ["password1", "password2"]:
            self.fields[field_name].help_text = None


class UserRegisterForm(BaseAuthForm):
    class Meta:
        model = UserModel
        fields = (UserBaseModel.USERNAME_FIELD, )


class UserLoginForm(BaseGenericForm):
    email = forms.CharField(
        widget=forms.EmailInput(
            attrs={"placeholder": "Email"}
        )
    )

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"placeholder": "Password"}
        )
    )

class UserEditForm(BaseModelForm):
    class Meta:
        model = UserProfileModel
        fields = (
            "first_name",
            "last_name",
            "age",
            "gender",
            "profile_picture",
        )
