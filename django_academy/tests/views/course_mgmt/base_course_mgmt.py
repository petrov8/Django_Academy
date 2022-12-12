from app_course.models import CourseModel
from django_academy.tests.base import BaseTestClass

sample_course_url = "https://miro.medium.com/max/696/1*hmvn5XYLGXrF4ACspVqgPw.png"


class BaseCourseView(BaseTestClass):

    course_details = {
        "title": "Test",
        "description": "Testing purposes",
        "technology": "Python",
        "dev_type": "Front End",
        "competency_level": "Beginner",
        "price": 450,
        "image_url": sample_course_url,
        "start_date": "25 Dec 2022"
    }

    @staticmethod
    def check_if_courses():
        return CourseModel.objects.all()

    @staticmethod
    def return_course(course_id):
        try:
            return CourseModel.objects.filter(id=course_id)[0]
        except Exception:
            return None




