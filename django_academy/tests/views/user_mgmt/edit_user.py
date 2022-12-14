from django_academy.tests.views.user_mgmt.base_user_mgmt import *


class EditProfileView(BaseTestUser):

    def test_edit_first_name__existing_user__with_correct_input(self):
        is_user_profile_completed = self.test_user.userprofilemodel.is_completed
        self.assertFalse(is_user_profile_completed)

        response = self.client.post(
            reverse("edit user", kwargs={"pk": 1}),
            {**self.profile_details}
        )

        first_name = response.wsgi_request.user.userprofilemodel.first_name
        is_user_profile_completed = response.wsgi_request.user.userprofilemodel.is_completed

        self.assertTrue(is_user_profile_completed)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.profile_details["first_name"], first_name)
        self.test_user.clean()

    #TODO: edit form validation error
    # def test_edit_first_name__existing_user__with_incorrect_input(self):
    #     self.profile_details["first_name"] = "11111"
    #
    #     with self.assertRaises(ValidationError):
    #         self.client.post(
    #             reverse("edit user", kwargs={"pk": 1}),
    #             {**self.profile_details}
    #         )
    #         self.test_user.clean()

    def test_edit_last_name__existing_user__with_correct_input(self):
        response = self.client.post(
            reverse("edit user", kwargs={"pk": 1}),
            {**self.profile_details}
        )

        last_name = response.wsgi_request.user.userprofilemodel.last_name
        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.profile_details["last_name"], last_name)
        self.test_user.clean()

    # TODO: edit form validation error
    # def test_edit_last_name__existing_user__with_incorrect_input(self):
    #     self.profile_details["last_name"] = "11111"
    #
    #     with self.assertRaises(ValidationError):
    #         self.client.post(
    #             reverse("edit user", kwargs={"pk": 1}),
    #             {**self.profile_details}
    #         )
    #         self.test_user.clean()

    def test_edit_age__existing_user__with_correct_input(self):
        response = self.client.post(
            reverse("edit user", kwargs={"pk": 1}),
            {**self.profile_details}
        )

        age = response.wsgi_request.user.userprofilemodel.age
        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.profile_details["age"], age)
        self.test_user.clean()

    # TODO: edit form validation error
    # def test_edit_age__existing_user__with_incorrect_input(self):
    #     self.profile_details["last_name"] = "11111"
    #
    #     with self.assertRaises(ValidationError):
    #         self.client.post(
    #             reverse("edit user", kwargs={"pk": 1}),
    #             {**self.profile_details}
    #         )
    #         self.test_user.clean()

    def test_edit_gender__existing_user__with_correct_input(self):
        response = self.client.post(
            reverse("edit user", kwargs={"pk": 1}),
            {**self.profile_details}
        )

        gender = response.wsgi_request.user.userprofilemodel.gender
        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.profile_details["gender"], gender)
        self.test_user.clean()

    # TODO: edit form validation error
    # def test_edit_gender__existing_user__with_incorrect_input(self):
    #     self.profile_details["last_name"] = "11111"
    #
    #     with self.assertRaises(ValidationError):
    #         self.client.post(
    #             reverse("edit user", kwargs={"pk": 1}),
    #             {**self.profile_details}
    #         )
    #         self.test_user.clean()

    def test_edit_profile_pic__existing_user__with_correct_url(self):
        response = self.client.post(
            reverse("edit user", kwargs={"pk": 1}),
            {**self.profile_details}
        )

        profiler = response.wsgi_request.user.userprofilemodel.profile_picture
        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.profile_details["profile_picture"], profiler)
        self.test_user.clean()

    # TODO: edit form validation exceptions
    # def test_edit_profile_pic__existing_user__with_incorrect_url(self):
    #     self.profile_details["last_name"] = "11111"
    #
    #     with self.assertRaises(ValidationError):
    #         self.client.post(
    #             reverse("edit user", kwargs={"pk": 1}),
    #             {**self.profile_details}
    #         )
    #         self.test_user.clean()


