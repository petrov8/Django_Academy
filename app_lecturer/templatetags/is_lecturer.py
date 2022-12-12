from support.base.template_tag import register
from support.add_funcs.user_support import UserSupport


@register.simple_tag(name="is_lecturer")
def is_lecturer(user):
    return UserSupport.check_if_lecturer(user)


