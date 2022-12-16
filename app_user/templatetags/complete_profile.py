from django.core.exceptions import ObjectDoesNotExist

from support.base.template_tag import register

@register.inclusion_tag("tags/complete_profile.html", takes_context=True)
def complete_profile_reminder(context):
    if context.request.user.pk is not None:
        completion_status = set()
        user = context.request.user

        completion_status.add(user.userprofilemodel.is_completed)
        try:
            completion_status.add(user.lecturermodel.is_completed)
        except ObjectDoesNotExist:
            pass

        return {
            "status": False if not all(completion_status) else True,
            "pk": user.pk,
            "role": user.role
        }







