from app_course.forms import CourseEditForm, CourseCreateForm
from app_course.models import CourseModel
from django.contrib import admin
from django.contrib.admin import ModelAdmin

@admin.register(CourseModel)
class CourseAdmin(ModelAdmin):
    list_display = ["title", "technology", "participants", "price"]
    list_filter = ["title", "technology", "price"]
    form = CourseEditForm
    add_form = CourseCreateForm

