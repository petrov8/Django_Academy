from functools import wraps

from django.shortcuts import redirect

from app_course.models import CourseModel
from app_user.enums import UserRoleEnum
from support.add_funcs.course_support import CourseSupport


class PermissionsDecors:

    @staticmethod
    def can_edit_course(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            kwargs["allowed"] = True
            user = args[0].request.user
            course = CourseModel.objects.filter(id=args[0].kwargs["pk"])[0]
            if not (
                    int(user.id) == int(course.creator_id) or
                    user.role == UserRoleEnum.admin.value or
                    user.role == UserRoleEnum.master.value
            ):
                kwargs["allowed"] = False
            return func(*args, **kwargs)
        return wrapper

    @staticmethod
    def can_edit_profile(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            kwargs["allowed"] = True
            user = args[0].request.user
            profile_id = args[0].kwargs["pk"]
            if not (
                    int(user.id) == int(profile_id) or
                    user.role == UserRoleEnum.admin.value or
                    user.role == UserRoleEnum.master.value
            ):
                kwargs["allowed"] = False
            return func(*args, **kwargs)
        return wrapper

    @staticmethod
    def can_edit_profile_func_view(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            user = args[0].user
            if not (
                    int(user.id) == int(kwargs["pk"]) or
                    user.role == UserRoleEnum.admin.value or
                    user.role == UserRoleEnum.master.value
            ):
                return redirect("permission denied")
            return func(*args, **kwargs)
        return wrapper

    @staticmethod
    def can_edit_course_func_view(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            user = args[0].user
            course = CourseSupport.return_course_object(kwargs["pk"])
            if not (
                    int(user.id) == int(course.creator_id) or
                    user.role == UserRoleEnum.admin.value or
                    user.role == UserRoleEnum.master.value
            ):
                return redirect("permission denied")
            return func(*args, **kwargs)
        return wrapper

