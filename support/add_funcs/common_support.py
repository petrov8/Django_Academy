from app_user.enums import UserRoleEnum


class CommonSupport:

    @staticmethod
    def check_forms_validity(*args):
        valid = True

        for form in args:
            if form and not form.is_valid():
                valid = False

        return valid

    @staticmethod
    def perform_perms_comparison(user, compare_against):
        if not (
                int(user.id) == int(compare_against) or
                user.role == UserRoleEnum.admin.value or
                user.role == UserRoleEnum.master.value
        ):
            return False
        return True