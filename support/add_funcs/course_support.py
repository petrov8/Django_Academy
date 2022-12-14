from functools import wraps

from django.http import Http404

from app_course.models import CourseModel
from app_user.enums import UserRoleEnum


class CourseSupport:

    @staticmethod
    def return_course_object(course_id):
        try:
            return CourseModel.objects.filter(id=course_id)[0]
        except IndexError:
            raise Http404

    @staticmethod
    def get_courses(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            user = args[0].request.user
            if user.role == UserRoleEnum.lecturer.value:
                kwargs["courses"] = CourseModel.objects.filter(creator_id=user.id).all()
            else:
                kwargs["courses"] = user.coursemodel_set.all()
            return func(*args, **kwargs)
        return wrapper

    @staticmethod
    def title_contains(value):
        return CourseModel.objects.filter(title__icontains=value)






