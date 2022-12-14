from django.contrib.auth import login, get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView

from app_user.forms import UserRegisterForm, UserEditForm
from app_user.models import UserProfileModel
from support.add_funcs.common_support import CommonSupport
from support.add_funcs.user_support import UserSupport
from support.base.base_views import BaseAuthView
from support.decors.permissions import PermissionsDecors
from support.mixins.mixins import GetSuccessUrlMixin
from support.mixins.auth_mixins import HasAccessToUserDetailsMixin

from django.contrib import messages


UserModel = get_user_model()

class NewUserView(CreateView):
    template_name = "users/new-user.html"
    form_class = UserRegisterForm
    success_url = reverse_lazy("catalogue")

    def form_valid(self, form):
        valid = super().form_valid(form)
        # form instance = self.object
        messages.success(self.request, "Registration successful.")
        login(self.request, self.object)
        return valid


class LoginUserView(GetSuccessUrlMixin, LoginView):
    template_name = "users/login-user.html"
    # form_class = UserLoginForm
    success_url = reverse_lazy("catalogue")


class LogoutUserView(LogoutView):
    next_page = reverse_lazy("index")


class ProfileUserView(BaseAuthView, HasAccessToUserDetailsMixin, DetailView):
    permission_required = [
        "app_user.view_userprofilemodel",
        "app_user.change_userprofilemodel"
    ]
    template_name = "users/profile.html"
    model = UserProfileModel

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        if UserSupport.check_if_lecturer(self.request.user):
            context["lecturer"] = UserSupport.return_lecturer_profile(self.request)
        return context


class DeleteUserView(BaseAuthView, HasAccessToUserDetailsMixin, DeleteView):
    permission_required = [
        "app_user.delete_userbasemodel"
    ]
    model = UserModel
    template_name = "users/delete-user.html"
    success_url = reverse_lazy("index")


def populate_user_edit_form(request, template, user_form, lecturer_form):
    return render(request, template, {
        "user_form": user_form,
        "lecturer_form": lecturer_form
    })


@login_required
@PermissionsDecors.can_edit_profile_func_view
def edit_user_view(request, pk):
    user_form = UserEditForm(
        request.POST or None, instance=UserSupport.return_user_profile(request))
    lecturer_form = UserSupport.return_lecturer_form(request)
    if request.method == "POST":
        validity = CommonSupport.check_forms_validity(user_form, lecturer_form)
        if validity:
            if lecturer_form:
                lecturer_form.save()
            user_form.save()
            messages.success(request, "Profile updated successfully")
            return redirect("profile user", pk)
        elif not validity:
            return populate_user_edit_form(request, "users/edit-user.html", user_form, lecturer_form)
    return populate_user_edit_form(request, "users/edit-user.html", user_form, lecturer_form)




