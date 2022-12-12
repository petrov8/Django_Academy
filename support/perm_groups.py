from django.contrib.auth.models import Group
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType


class GroupsMgmt:

    created_status = None

    """
    0 = students group
    1 = lecturers group
    2 = admins group
    3 = super users group
    """

    def __init__(self):
        self.permissions = ()
        self.groups = []

    def create_groups(self, group_names_enum):
        group_names = [x.value for x in group_names_enum]
        for name in group_names:
            new_group = Group.objects.get_or_create(name=name)[0]
            self.groups.append(new_group)

    def get_model_permissions(self, model):
        content_type = ContentType.objects.get_for_model(model)
        self.permissions = Permission.objects.filter(content_type=content_type)

    def assign_perms_to_groups(self):
        for perm in self.permissions:
            # core = lecturers + super_users
            if perm.codename == "add_coursemodel":
                self.groups[1].permissions.add(perm)
                self.groups[3].permissions.add(perm)

            # core = lecturers + admins + super_users
            elif perm.codename == "delete_coursemodel":
                self.groups[1].permissions.add(perm)
                self.groups[2].permissions.add(perm)
                self.groups[3].permissions.add(perm)

            # core = lecturers + admins + super_users
            elif perm.codename == "change_coursemodel":
                self.groups[1].permissions.add(perm)
                self.groups[2].permissions.add(perm)
                self.groups[3].permissions.add(perm)

            # core = students + lecturers + admins + super_users
            elif perm.codename == "view_coursemodel":
                self.groups[0].permissions.add(perm)
                self.groups[1].permissions.add(perm)
                self.groups[2].permissions.add(perm)
                self.groups[3].permissions.add(perm)

    @staticmethod
    def update_status():
        return True






# def create_groups():
#     # student_group, student_created = Group.objects.get_or_create(name="Student")
#     # lecturer_group, lecturer_created = Group.objects.get_or_create(name="Lecturer")
#     # admin_group, admin_created = Group.objects.get_or_create(name="Admin")
#     # super_user_group, super_created = Group.objects.get_or_create(name="Super User")
#
#
#
#     for perm in course_permissions:
#         if perm.codename == "add_coursemodel":
#             lecturer_group.permissions.add(perm)
#             super_user_group.permissions.add(perm)
#
#         elif perm.codename == "delete_coursemodel":
#             admin_group.permissions.add(perm)
#             lecturer_group.permissions.add(perm)
#             super_user_group.permissions.add(perm)
#
#         elif perm.codename == "edit_coursemodel":
#             lecturer_group.permissions.add(perm)
#             admin_group.permissions.add(perm)
#             super_user_group.permissions.add(perm)
#
#         elif perm.codename == "view_coursemodel":
#             student_group.permissions.add(perm)
#             lecturer_group.permissions.add(perm)
#             admin_group.permissions.add(perm)
#             super_user_group.permissions.add(perm)