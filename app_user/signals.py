from django.contrib.auth import get_user_model, user_logged_in
from django.contrib.auth.models import Group
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from app_course.models import CourseModel
from app_lecturer.models import LecturerModel
from app_user.enums import UserRoleEnum
from app_user.models import UserProfileModel
from support.add_funcs.user_support import UserSupport
from support.perm_groups import PermGroupsMgmt

BaseModel = get_user_model()

def generate_permission_groups(sender, **kwargs):
    models = [LecturerModel, CourseModel, BaseModel, UserProfileModel]
    perms = PermGroupsMgmt()
    perms.create_groups(UserRoleEnum)

    for next_model in models:
        perms.get_model_permissions(next_model)


@receiver(pre_save, sender=UserProfileModel)
def is_user_profile_completed(sender, instance, **kwargs):
    instance.is_completed = True

    if not UserSupport.check_if_fields_are_updated(instance, exceptions=["is_completed"]):
        instance.is_completed = False


@receiver(post_save, sender=BaseModel)
def create_user_profile(sender, instance, created, **kwargs):

    if created:
        return UserProfileModel.objects.create(user=instance)


@receiver(post_save, sender=BaseModel)
def assign_user_to_group(sender: BaseModel, instance: BaseModel, **kwargs) -> None:

    """
    Every user can be assigned to a single group (conditional on user.role)
    In case a user has already been assigned to a group but user.role had been updated meanwhile:
        - remove current group (Student by default) and reassign user to new one. 
    concern: PermissionsMixin will pick up old group => 403 Forbidden 
    """
    #TODO: what happens if you downgrade user.role ?
    if len(instance.groups.all()) > 1:
        remove_group = Group.objects.get(name=UserRoleEnum.student.value)
        instance.groups.remove(remove_group)
    group = Group.objects.get(name=instance.role)
    if group not in instance.groups.all():
        group.user_set.add(instance)

@receiver(user_logged_in, sender=BaseModel)
def admin_team_mgmt(user, **kwargs) -> None:
    if user.is_staff and user.role == UserRoleEnum.student.value:
        if user.is_superuser:
            user.role = "Master"
        else:
            user.role = "Admin"
        user.save()
















