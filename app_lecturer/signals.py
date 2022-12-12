from django.contrib.auth import get_user_model
from django.contrib.auth.signals import user_logged_in
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver

from app_lecturer.models import LecturerModel
from support.add_funcs.user_support import UserSupport

BaseModel = get_user_model()

"""
Upon every login:
0 - every user is initially set-up as 'student'. Admins change category to 'Lecturer' manually. 
1 - check if user category has been changed to lecturer 
2 - if yes, check if lecturer has a lecturer profile already
3 - if yes, leave
4 - if lecturer doesn't have a profile, set one up (lecurer will be reminded to complete until profile.is_completed = True
"""


@receiver(pre_save, sender=LecturerModel)
def is_lecturer_profile_completed(sender, instance, **kwargs):
    instance.is_completed = True

    if not UserSupport.check_if_fields_are_updated(instance, exceptions=["is_completed", "coursemodel"]):
        instance.is_completed = False


@receiver(user_logged_in, sender=BaseModel)
def check_if_lecturer_profile(user, **kwargs):
    if UserSupport.check_if_lecturer(user):
        try:
            _lecturer_profile = LecturerModel.objects.filter(user_id=user.id)[0]
            return
        except:
            # do not use ObjectDoesNotExist exception. Does not execute next line!
            return LecturerModel.objects.create(user=user)

