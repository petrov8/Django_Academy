from django.http import Http404

from app_lecturer.forms import LecturerEditForm
from app_lecturer.models import LecturerModel
from app_user.enums import UserRoleEnum
from app_user.models import UserProfileModel


class UserSupport:

    @staticmethod
    def check_if_lecturer(user):
        if user.role == UserRoleEnum.lecturer.value:
            return True
        return False

    @staticmethod
    def check_if_student(user):
        if user.role == UserRoleEnum.student.value:
            return True
        return False

    @staticmethod
    def return_user_profile(user):
        try:
            return UserProfileModel.objects.filter(user_id=user.id)[0]
        except Exception:
            raise Http404

    @staticmethod
    def return_lecturer_profile(user):
        try:
            return LecturerModel.objects.filter(user_id=user.id)[0]
        except IndexError:
            return Http404


    @staticmethod
    def return_lecturer_form(request):
        if UserSupport.check_if_lecturer(request.user):
            return LecturerEditForm(
                request.POST or None, instance=UserSupport.return_lecturer_profile(request.user)
            )
        return None


    @staticmethod
    def check_if_fields_are_updated(obj, exceptions: list):
        for field in obj._meta.get_fields():
            if field.name not in exceptions and not getattr(obj, field.name):
                return False
        return True


