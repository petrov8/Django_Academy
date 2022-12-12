from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView

from app_course.forms import CourseCreateForm, CourseEditForm, CourseDeleteForm
from app_course.models import CourseModel
from support.add_funcs.common_support import CommonSupport
from support.add_funcs.course_support import CourseSupport
from support.base.base_views import BaseAuthView, BaseEditCourseView
from support.decors.permissions import PermissionsDecors


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


def populate_course_view(request, form, pk):
    return render(request, "courses/edit-course.html", {
        "form": form,
        "pk": pk
    })

@login_required
@PermissionsDecors.can_edit_course_func_view
def edit_course_view(request, pk):
    course = CourseSupport.return_course_object(pk)
    course_form = CourseEditForm(request.POST or None, instance=course)
    if request.method == "POST":
        if CommonSupport.check_forms_validity(course_form):
            course_form.save()
            return redirect("catalogue")
        return populate_course_view(request, course_form, pk)
    return populate_course_view(request, course_form, pk)


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
