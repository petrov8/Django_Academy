from django.contrib.auth import get_user_model
from django.core.exceptions import PermissionDenied

from support.add_funcs.common_support import CommonSupport
from support.add_funcs.course_support import CourseSupport

UserModel = get_user_model()


class CanPerformCourseEditMixin:
    def dispatch(self, request, *args, **kwargs):
        user = request.user
        course = CourseSupport.return_course_object(kwargs["pk"])
        if not CommonSupport.perform_perms_comparison(user,course.creator_id):
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


class HasAccessToUserDetailsMixin:
    def dispatch(self, request, *args, **kwargs):
        user = request.user
        profile_id = kwargs["pk"]
        if not CommonSupport.perform_perms_comparison(user, profile_id):
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)