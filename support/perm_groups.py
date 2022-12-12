from django.contrib.auth.models import Group
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType


class PermGroupsMgmt:

    created_status = None
    perm_groups = []

    models_mapping = {
        "CourseModel": "course",
        "UserProfileModel": "userprofile",
        "UserBaseModel": "userbase",
        "LecturerModel": "lecturer"
    }

    def __init__(self):
        self.permissions = ()
        self.groups = PermGroupsMgmt.perm_groups

    @staticmethod
    def create_groups(group_names_enum):
        group_names = [x.value for x in group_names_enum]
        for name in group_names:
            new_group = Group.objects.get_or_create(name=name)[0]
            PermGroupsMgmt.perm_groups.append(new_group)


    def get_model_permissions(self, model):
        content_type = ContentType.objects.get_for_model(model)
        self.permissions = Permission.objects.filter(content_type=content_type)
        model_name = PermGroupsMgmt.models_mapping[model.__name__]

        self.assign_perms_to_groups(model_name)

    def assign_perms_to_groups(self, value):

        """
        0 = students group
        1 = lecturers group
        2 = admins group
        3 = masters group
        """

        for perm in self.permissions:

            # view -> all types of users can perform full 'view' on all models.

            if perm.codename == f"view_{value}model":
                self.groups[0].permissions.add(perm)
                self.groups[1].permissions.add(perm)
                self.groups[2].permissions.add(perm)
                self.groups[3].permissions.add(perm)

            # add -> only admins and master users can perform full 'add' on all models
                # students cannot add
                # lecturers can only add courses

            if perm.codename == f"add_{value}model":
                if perm.codename == "add_coursemodel":
                    self.groups[1].permissions.add(perm)
                self.groups[2].permissions.add(perm)
                self.groups[3].permissions.add(perm)

            # change -> only admins and master users can perform full 'change' on all models
                # students can only change their profiles
                # lecturers can only change their userprofiles, courses and lecturer profiles

            elif perm.codename == f"change_{value}model":
                if perm.codename in ["change_userprofilemodel", "change_userbasemodel"] :
                    self.groups[0].permissions.add(perm)
                    self.groups[1].permissions.add(perm)
                if perm.codename in ["change_coursemodel", "change_lecturermodel"]:
                    self.groups[1].permissions.add(perm)
                self.groups[2].permissions.add(perm)
                self.groups[3].permissions.add(perm)

            # delete -> only master users can perform full 'delete' on all models (other users included)
                # students can delete their accounts/profiles
                # lecturers can delete their accounts/profiles and courses
                # admins can delete their accounts/profiles and courses (admins cannot delete master users)

            elif perm.codename == f"delete_{value}model":
                if perm.codename in ["delete_userbasemodel"]:
                    self.groups[0].permissions.add(perm)
                    self.groups[1].permissions.add(perm)
                    self.groups[2].permissions.add(perm)
                if perm.codename == "delete_coursemodel":
                    self.groups[1].permissions.add(perm)
                    self.groups[2].permissions.add(perm)
                if perm.codename == "delete_lecturermodel":
                    self.groups[1].permissions.add(perm)
                self.groups[3].permissions.add(perm)


    @staticmethod
    def update_status():
        return True






