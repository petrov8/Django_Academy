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
            raise IndexError("User could not be found.")

    @staticmethod
    def return_lecturer_profile(user):
        try:
            return LecturerModel.objects.filter(user_id=user.id)[0]
        except Exception:
            raise IndexError(
                "Lecturer could not be found. Was this profile role recently updated ?"
                "If so, please log out and log back in again for changed to take place")

    @staticmethod
    def check_if_fields_are_updated(obj, exceptions: list):
        for field in obj._meta.get_fields():
            if field.name not in exceptions and not getattr(obj, field.name):
                return False
        return True


