
from django_academy.tests.views.user_mgmt.base_user_mgmt import *


class NewLecturerProfileSignal(BaseTestUser):

    def test_register_signal__new_lecturer_profile__correct_details(self):
        lecturer_profile = super().lecturer_exists()
        self.assertEqual(lecturer_profile, False)

        self.test_user = super().change_user_role_to_lecturer()

        self.client.login(**self.credentials)
        lecturer_profile = super().lecturer_exists()
        self.assertIsNotNone(lecturer_profile)
        self.assertEqual(lecturer_profile.user_id, self.test_user.id)

        self.test_user.full_clean()

