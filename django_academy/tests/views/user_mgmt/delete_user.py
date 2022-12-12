from django_academy.tests.views.user_mgmt.base_user_mgmt import *


class DeleteProfileView(BaseTestUser):

    def test_delete_profile__existing_user(self):
        test_user = super().user_exists()
        profile = super().profile_exists()
        self.assertEqual(test_user.is_active, True)
        self.assertEqual(test_user.is_authenticated, True)
        self.assertEqual(profile.user.is_active, True)

        response = self.client.post(reverse("delete user", kwargs={"pk": self.test_user.pk}))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(super().user_exists())
        self.assertFalse(super().profile_exists())

        test_user.full_clean()



