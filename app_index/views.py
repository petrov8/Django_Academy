from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from app_course.models import CourseModel
from support.add_funcs.course_support import CourseSupport


class HomePage(TemplateView):
    template_name = "base.html"


class CataloguePage(LoginRequiredMixin, ListView):
    model = CourseModel
    template_name = "index_home/catalogue.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context["courses"] = \
            CourseModel.objects.all()
        return context


def search_view(request):
    if request.method == "POST":
        criterion = request.POST["target"]
        matches = CourseSupport.title_contains(criterion)
        return render(request, "index_home/search.html", {
            "object_list": matches,
            "criterion": None if not criterion else criterion
        })
    return render(request, "index_home/search.html", {})

