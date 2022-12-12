from django.urls import path, include

import app_course.views as resource

urlpatterns = [
    path("new/", resource.PublishCourseView.as_view(), name="new course"),
    path("courses/", resource.MyCoursesView.as_view(), name="my courses"),
    path("<int:pk>/", include([
        # path("take/", resource.TakeCourseView.as_view(), name="take course"),
        # path("take/", resource.take_course_view, name="take course"),
        path("opt-out/", resource.remove_course_view, name="opt-out from course"),
        path("info/", resource.DetailsCourseView.as_view(), name="details course"),
        path("edit/", resource.EditCourseView.as_view(), name="edit course"),
        path("delete/", resource.DeleteCourseView.as_view(), name="delete course"),
        ])
    )
]

