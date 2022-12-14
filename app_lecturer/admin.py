from django.contrib import admin
from django.contrib.admin import ModelAdmin

from app_course.models import CourseModel
from app_lecturer.forms import LecturerRegisterForm, LecturerEditForm
from app_lecturer.models import LecturerModel

@admin.register(LecturerModel)
class LecturerAdmin(ModelAdmin):
    list_display = ["email", "full_name", "fav_language", "is_completed", "courses", "students"]
    list_filter = ["fav_language", "is_completed"]
    form = LecturerEditForm
    add_form = LecturerRegisterForm

    def email(self, obj):
        return obj.user.email

    def full_name(self, obj):
        return f"{obj.user.userprofilemodel.first_name} {obj.user.userprofilemodel.last_name}"

    def courses(self, obj):
        return len(CourseModel.objects.filter(creator_id=obj.user.id).all())

    def students(self, obj):
        total = 0
        courses = CourseModel.objects.filter(creator_id=obj.user.id).all()
        if courses:
            total = sum([course.participants for course in courses])
        return total

