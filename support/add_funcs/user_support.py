from django.contrib import messages

from app_lecturer.forms import LecturerEditForm
from app_lecturer.models import LecturerModel
from app_user.enums import UserRoleEnum
from app_user.models import UserProfileModel


class UserSupport:

    @staticmethod
    def return_user_profile(request):
        try:
            return UserProfileModel.objects.filter(user_id=request.user.id)[0]
        except Exception as ex:
            messages.error(request, "Could not find user.")
            return None

    @staticmethod
    def return_lecturer_profile(request):
        a = 5
        try:
            return LecturerModel.objects.filter(user_id=request.user.id)[0]
        except IndexError:
            messages.error(request,
                           "Lecturer profile does not exist. "
                           "In case your profile was just upgraded to 'Lecturer' - log out and back in again for "
                           "changes to take effect")
            return None

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
    def return_lecturer_form(request):
        if UserSupport.check_if_lecturer(request.user):
            return LecturerEditForm(
                request.POST or None, instance=UserSupport.return_lecturer_profile(request)
            )
        return None


    @staticmethod
    def check_if_fields_are_updated(obj, exceptions: list):
        for field in obj._meta.get_fields():
            if field.name not in exceptions and not getattr(obj, field.name):
                return False
        return True


