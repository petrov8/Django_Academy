from support.base.template_tag import register

from support.add_funcs.user_support import UserSupport


@register.inclusion_tag("tags/complete_profile.html", takes_context=True)
def complete_profile_reminder(context):
    if context.request.user.pk is not None:
        completion_status = set()
        user = context.request.user
        completion_status.add(user.userprofilemodel.is_completed)

        if UserSupport.check_if_lecturer(user):
            completion_status.add(user.lecturermodel.is_completed)

        return {
            "status": False if not all(completion_status) else True,
            "pk": user.pk,
            "role": user.role
        }







