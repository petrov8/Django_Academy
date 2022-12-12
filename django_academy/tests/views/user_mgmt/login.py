from django_academy.tests.views.user_mgmt.base_user_mgmt import *


class TestLoginView(BaseTestUser):

    def test_user__login_with_correct_details(self):
        self.credentials["email"] = "test@abv.bg"
        new_user = super().create_test_user()

        self.client.login(**self.credentials)

        response = self.client.get(reverse("catalogue"))
        self.assertEqual(new_user, response.context["user"])

    def test_user__login_with_wrong_password(self):
        self.client.logout()
        self.test_user.full_clean()

        self.credentials["password"] = "wrong"
        self.client.login(**self.credentials)

        response = self.client.get(reverse("catalogue"))

        self.assertEqual(response.status_code, 302)
        self.assertFalse(response.wsgi_request.user.is_authenticated)

    def test_user__login_with_wrong_username(self):
        self.client.logout()
        self.test_user.full_clean()

        self.credentials["username"] = "wrong@abv.bg"
        self.client.login(**self.credentials)

        response = self.client.get(reverse("catalogue"))

        self.assertEqual(response.status_code, 302)
        self.assertFalse(response.wsgi_request.user.is_authenticated)


















