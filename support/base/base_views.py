from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import redirect

from support.decors.permissions import PermissionsDecors


class BaseAuthView(LoginRequiredMixin, PermissionRequiredMixin):
    permission_denied_message = "You are not authorized to perform this action."


class BaseEditCourseView(BaseAuthView):

    @PermissionsDecors.can_edit_course
    def has_permission(self, **kwargs):
        perms = super().has_permission()
        if perms and not kwargs["allowed"]:
            return redirect("permission denied")
        return perms


class BaseEditUserView(BaseAuthView):

    @PermissionsDecors.can_edit_profile
    def has_permission(self, **kwargs):
        perms = super().has_permission()
        if perms and not kwargs["allowed"]:
            return redirect("permission denied")
        return perms

