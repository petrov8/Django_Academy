from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.contrib.auth import admin as auth_admin, get_user_model

from app_user.enums import UserRoleEnum
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
    list_filter = ("email", "role", "is_staff", "is_superuser" )
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
    list_display = ["email", "role", "full_name", "age", "gender", "is_completed", "subscriptions", "avg_spent"]
    list_filter = ["age", "gender", "is_completed"]
    form = UserEditForm
    add_form = UserEditForm

    def role(self, obj):
        return obj.user.role

    def email(self, obj):
        return obj.user.email

    def full_name(self, obj):
        return f"{obj.user.userprofilemodel.first_name} {obj.user.userprofilemodel.last_name}"

    def subscriptions(self, obj):
        if obj.user.role == UserRoleEnum.student.value:
            return len(obj.user.coursemodel_set.all())
        return "not student"

    def avg_spent(self, obj):
        if obj.user.role == UserRoleEnum.student.value:
            avg = 0
            if obj.user.coursemodel_set.all():
                avg = sum([course.price for course in obj.user.coursemodel_set.all()])
            return avg
        return "not student"






