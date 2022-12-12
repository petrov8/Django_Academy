from django_academy.tests.views.course_mgmt.base_course_mgmt import *
from django_academy.tests.views.user_mgmt.base_user_mgmt import *


class PublishCourseView(BaseTestUser, BaseCourseView):

    def test_delete_course__by_lecturer__correct_perms(self):
        self.test_user = super().change_user_role_to_lecturer()

        response = self.client.post(reverse("new course"), {
            **BaseCourseView.course_details
        })

        # 302 = course created and page redirected to catalogue
        self.assertEqual(response.status_code, 302)
        courses = len(BaseCourseView.check_if_courses())
        self.assertEqual(courses, 1)

        response_2 = self.client.post(reverse("delete course", kwargs={"pk": 1}), **BaseCourseView.course_details)
        self.assertEqual(response_2.status_code, 200)
        self.test_user.full_clean()

    def test_delete_course__by_admin__correct_perms(self):
        self.test_user = super().change_user_role_to_lecturer()

        response = self.client.post(reverse("new course"), {
            **BaseCourseView.course_details
        })

        self.client.logout()

        self.credentials["email"] = "test@abv.bg"
        second_user = super().create_test_user()
        second_user.role = "Admin"
        second_user.user_permissions.add(35)
        second_user.save()
        self.client.login(**self.credentials)

        # 302 = course created and page redirected to catalogue
        self.assertEqual(response.status_code, 302)
        courses = len(BaseCourseView.check_if_courses())
        self.assertEqual(courses, 1)

        response_2 = self.client.post(reverse("delete course", kwargs={"pk": 1}))
        self.assertEqual(response_2.status_code, 200)
        self.test_user.full_clean()


