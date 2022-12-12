from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView, ListView

from app_course.forms import CourseCreateForm, CourseEditForm, CourseDeleteForm
from app_course.models import CourseModel
from support.add_funcs.course_support import CourseSupport
from support.base.base_views import BaseAuthView, BaseEditCourseView


class PublishCourseView(BaseAuthView, CreateView):
    permission_required = ["app_course.add_coursemodel"]

    model = CourseModel
    template_name = "courses/new-course.html"
    form_class = CourseCreateForm
    success_url = reverse_lazy("catalogue")

    def form_valid(self, form):
        form.instance.creator_id = self.request.user.id
        return super().form_valid(form)


class DetailsCourseView(BaseAuthView, DetailView):
    permission_required = ["app_course.view_coursemodel"]
    model = CourseModel
    template_name = "courses/details-course.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context["course_added"] = False
        course = kwargs["object"]
        if course in self.request.user.coursemodel_set.all():
            context["course_added"] = True
        return context


class EditCourseView(BaseEditCourseView, UpdateView):
    permission_required = ["app_course.change_coursemodel"]
    template_name = "courses/edit-course.html"
    model = CourseModel
    form_class = CourseEditForm
    success_url = reverse_lazy("catalogue")


class DeleteCourseView(BaseEditCourseView, DeleteView):
    permission_required = ["app_course.delete_coursemodel"]
    model = CourseModel
    form_class = CourseDeleteForm
    template_name = "courses/delete-course.html"
    success_url = reverse_lazy("catalogue")

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({
            'instance': CourseSupport.return_course_object(self.kwargs["pk"])
        })
        return kwargs


class MyCoursesView(BaseAuthView, ListView):
    permission_required = ["app_course.view_coursemodel"]
    model = CourseModel
    template_name = "courses/my-courses.html"

    @CourseSupport.get_courses
    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context["courses"] = kwargs["courses"]
        return context


@login_required
def remove_course_view(request, **kwargs):
    user = request.user
    course = CourseSupport.return_course_object(kwargs["pk"])
    if course in user.coursemodel_set.all():
        course.students.remove(user.id)
        course.participants -= 1
        course.save()
        return redirect("my courses")



# Done via payment view
# class TakeCourseView(BaseAuthView, DetailView):
#     permission_required = ["app_course.view_coursemodel"]
#     model = CourseModel
#     template_name = "courses/take-course.html"
#
#     def post(self, request, *args,  **kwargs):
#         self.object = self.get_object()
#         user = self.request.user
#         if UserSupport.check_if_student(user):
#             course = self.object
#             course.students.add(user)
#             user.coursemodel_set.add(course)
#             course.participants += 1
#             course.save()
#         return render(request, "courses/my-courses.html", {
#             "courses": user.coursemodel_set.all()
#         })


