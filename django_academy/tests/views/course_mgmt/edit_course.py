
from django_academy.tests.views.course_mgmt.base_course_mgmt import *
from django_academy.tests.views.user_mgmt.base_user_mgmt import *


class PublishCourseView(BaseTestUser, BaseCourseView):

    def test_publish_course__by_lecturer__correct_perms(self):
        self.test_user = super().change_user_role_to_lecturer()

        response = self.client.post(reverse("new course"), {
            **BaseCourseView.course_details
        })

        # 302 = course created and page redirected to catalogue
        self.assertEqual(response.status_code, 302)
        courses = len(BaseCourseView.check_if_courses())

        # confirm course exists
        self.assertEqual(courses, 1)

        # edit course details
        BaseCourseView.course_details["price"] = 10
        BaseCourseView.course_details["title"] = "Updated"

        # push change
        response_2 = self.client.post(reverse("edit course", kwargs={"pk": 1}), {**BaseCourseView.course_details})

        course = BaseCourseView.return_course(1)
        self.assertEqual(course.title, "Updated")
        self.assertEqual(response_2.status_code, 302)
        self.test_user.full_clean()
        course.full_clean()

    def test_publish_course__by_lecturer__no_perms(self):
        self.test_user = super().change_user_role_to_lecturer()

        course_1 = self.client.post(reverse("new course"), {
            **BaseCourseView.course_details
        })

        self.client.logout()

        # 302 = course created and page redirected to catalogue
        self.assertEqual(course_1.status_code, 302)
        courses = len(BaseCourseView.check_if_courses())

        # confirm course exists
        self.assertEqual(courses, 1)

        # init second lecturer
        self.credentials["email"] = "test@abv.bg"
        second_user = super().create_test_user()
        second_user.role = "Lecturer"
        second_user.user_permissions.add(34)
        second_user.save()
        self.client.login(**self.credentials)

        # edit course details
        BaseCourseView.course_details["price"] = 10
        BaseCourseView.course_details["title"] = "Updated"

        # push change
        response_2 = self.client.post(reverse("edit course", kwargs={"pk": 1}), {**BaseCourseView.course_details})

        course = BaseCourseView.return_course(1)
        # old title
        self.assertEqual(course.title, "Test")
        # rejected / not authorized
        self.assertEqual(response_2.status_code, 403)
        self.test_user.full_clean()

