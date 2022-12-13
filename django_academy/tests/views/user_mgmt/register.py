from django_academy.tests.views.user_mgmt.base_user_mgmt import *


class NewUserViewTestCase(BaseTestUser):

    def test_register__new_user__with_correct_input(self):
        response = self.client.post(
            reverse("new user"),
            {**self.credentials}
        )

        test_user = response.wsgi_request.user

        self.assertIsNotNone(test_user.pk)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "users/new-user_2.html")
        test_user.full_clean()

    def test_register__new_user__profile_creation_success(self):
        response = self.client.post(
            reverse("new user"),
            {**self.credentials}
        )
        test_user = response.wsgi_request.user
        profile = UserProfileModel.objects.filter(user_id=test_user.id)[0]

        self.assertEquals(profile.user_id, test_user.id)
        test_user.full_clean()

    def test_register__new_user__when_email_already_taken(self):
        with self.assertRaises(Exception) as error:
            user_1 = super().create_test_user()
            user_1.full.clean()

        self.assertEqual(IntegrityError, type(error.exception))

    def test_register__new_user__with_wrong_email(self):
        self.credentials["email"] = "doncho"
        test_user = super().create_test_user()

        with self.assertRaises(ValidationError) as error:
            test_user.full_clean()
            test_user.save()

        self.assertEqual("{'email': ['Enter a valid email address.']}", str(error.exception))

    # #will create / regulated by form validator
    # def test_register__new_user__with_wrong_password(self):
    #     credentials = {
    #         "email": "doncho@abv.bg",
    #         "password": ""
    #     }
    #     with self.assertRaises(ValidationError) as error:
    #         response = self.client.post(
    #             reverse("new user"),
    #             {**credentials}
    #         )
    #         response.full_clean()
    #
    #     print(response)
