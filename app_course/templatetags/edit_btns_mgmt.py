from support.base.template_tag import register
from app_user.enums import UserRoleEnum


@register.simple_tag(name="show_buttons")
def show_buttons(user, course):
    if user.id == course.creator_id or user.role == UserRoleEnum.master.value or user.role == UserRoleEnum.admin.value:
        return True
    return False




