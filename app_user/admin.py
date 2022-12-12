from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.contrib.auth import admin as auth_admin, get_user_model

from app_lecturer.forms import LecturerRegisterForm, LecturerEditForm
from app_lecturer.models import LecturerModel
from app_user.forms import UserEditForm, UserRegisterForm
from app_user.models import UserProfileModel

UserModel = get_user_model()


@admin.register(UserModel)
class UserAdmin(auth_admin.UserAdmin):

    add_form = UserRegisterForm
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2"),
            },
        ),
    )
    list_display = [
        "email",
        "is_staff",
        "is_superuser",
        "role",
        "last_login",
    ]
    list_filter = ("email", )
    search_fields = ()
    ordering = ("email", )
    filter_horizontal = ()
    fieldsets = (
        (
            None,
            {
                'fields': (
                    'email',
                    'password',
                ),
            }),
        (
            'Personal info',
            {
                'fields': (
                    'role',
                ),
            },
        ),
        (
            'Permissions',
            {
                'fields': (
                    'is_staff',
                    'is_superuser',
                    'user_permissions',
                ),
            },
        ),
        (
            'Important dates',
            {
                'fields': (
                    'last_login',
                ),
            },
        ),
    )


@admin.register(UserProfileModel)
class ProfileAdmin(ModelAdmin):
    list_display = ["email", "full_name"]
    form = UserEditForm
    add_form = UserEditForm

    def email(self, obj):
        a = 5
        return obj.user.email

    def full_name(self, obj):
        print(obj.user.userprofilemodel.first_name)
        return f"{obj.user.userprofilemodel.first_name} {obj.user.userprofilemodel.last_name}"


@admin.register(LecturerModel)
class ProfileAdmin(ModelAdmin):
    list_display = ["email", "full_name"]
    form = LecturerEditForm
    add_form = LecturerRegisterForm

    def email(self, obj):
        a = 5
        return obj.user.email

    def full_name(self, obj):
        print(obj.user.userprofilemodel.first_name)
        return f"{obj.user.userprofilemodel.first_name} {obj.user.userprofilemodel.last_name}"



