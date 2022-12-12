from django_academy.tests.views.lecturer_mgmt.lecturer_mgmt import BaseLecturerUser
from django_academy.tests.views.user_mgmt.base_user_mgmt import *


class EditLecturerProfileView(BaseTestUser, BaseLecturerUser):

    def test_edit_lecturer_profile__existing_user__with_correct_input(self):
        self.test_user = super().change_user_role_to_lecturer()

        fav_language = self.test_user.lecturermodel.fav_language
        is_lecturer_profile_completed = self.test_user.lecturermodel.is_completed
        self.assertEqual("Select", fav_language)
        self.assertFalse(is_lecturer_profile_completed)

        response = self.client.post(
            reverse("edit user", kwargs={"pk": 1}),
            {**BaseLecturerUser.lecturer_details}
        )

        self.assertEqual(response.status_code, 302)
        fav_language = response.wsgi_request.user.lecturermodel.fav_language
        is_lecturer_profile_completed = response.wsgi_request.user.lecturermodel.is_completed
        self.assertEqual("Python", fav_language)
        self.assertTrue(is_lecturer_profile_completed)
        self.test_user.clean()

