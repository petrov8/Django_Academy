from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


class BaseAuthView(LoginRequiredMixin, PermissionRequiredMixin):
    pass




