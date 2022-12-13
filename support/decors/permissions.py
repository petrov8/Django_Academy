from functools import wraps

from django.shortcuts import redirect
from support.add_funcs.common_support import CommonSupport
from support.add_funcs.course_support import CourseSupport


class PermissionsDecors:

    @staticmethod
    def can_edit_profile_func_view(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            user = args[0].user
            if not CommonSupport.perform_perms_comparison(user, kwargs["pk"]):
                return redirect("permission denied")
            return func(*args, **kwargs)
        return wrapper


    @staticmethod
    def can_edit_course_func_view(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            user = args[0].user
            course = CourseSupport.return_course_object(kwargs["pk"])
            if not CommonSupport.perform_perms_comparison(user, course.creator_id):
                return redirect("permission denied")
            return func(*args, **kwargs)
        return wrapper

