from django_academy.tests.views.user_mgmt.base_user_mgmt import *


class UserPermissionsGroupSignal(BaseTestUser):

    def test_permission_signal__existing_user__student_to_admin(self):

        self.credentials["email"] = "student@abv.bg"
        student = super().create_test_user()

        response = self.client.get(reverse("profile user", kwargs={"pk": student.id}))

        self.test_user.role = "Admin"
        self.test_user.save()

        response_2 = self.client.get(reverse("profile user", kwargs={"pk": student.id}))

        # check if permissions assignment works
        self.assertTrue(self.test_user.groups.filter(name="Admin").exists())
