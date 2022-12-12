from django.contrib.auth import login, get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView

from app_lecturer.forms import LecturerEditForm
from app_user.forms import UserRegisterForm, UserEditForm
from app_user.models import UserProfileModel
from support.add_funcs.user_support import UserSupport
from support.base.base_views import BaseEditUserView, BaseAuthView
from support.decors.permissions import PermissionsDecors
from support.mixins.mixins import GetSuccessUrlMixin

UserModel = get_user_model()

no_access_msg = "You cant"


class NewUserView(CreateView):
    template_name = "users/new-user.html"
    form_class = UserRegisterForm
    success_url = reverse_lazy("index")

    def form_valid(self, form):
        valid = super().form_valid(form)
        # form instance = self.object
        login(self.request, self.object)
        return valid


class LoginUserView(GetSuccessUrlMixin, LoginView):
    template_name = "users/login-user.html"
    success_url = reverse_lazy("catalogue")


class LogoutUserView(LogoutView):
    next_page = reverse_lazy("index")


class ProfileUserView(BaseAuthView, DetailView):
    permission_required = []
    template_name = "users/profile.html"
    model = UserProfileModel

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        if UserSupport.check_if_lecturer(self.request.user):
            context["lecturer"] = UserSupport.return_lecturer_profile(self.request.user)
        return context


@login_required
@PermissionsDecors.can_edit_profile_func_view
def edit_user_view(request, pk):
    user_form = UserEditForm(
        request.POST or None, instance=UserSupport.return_user_profile(request.user))
    lecturer_form = return_lecturer_form(request)
    if request.method == "POST":
        if lecturer_form and lecturer_form.is_valid():
            lecturer_form.save()
        if user_form.is_valid():
            user_form.save()
        return redirect("profile user", pk)
    return render(request, "users/edit-user.html", {
        "user_form": user_form,
        "lecturer_form": lecturer_form
    })


def return_lecturer_form(request):
    if UserSupport.check_if_lecturer(request.user):
        return LecturerEditForm(
            request.POST or None, instance=UserSupport.return_lecturer_profile(request.user)
        )
    return None


class DeleteUserView(BaseEditUserView, DeleteView):
    permission_required = []

    model = UserModel
    template_name = "users/delete-user.html"
    success_url = reverse_lazy("index")





