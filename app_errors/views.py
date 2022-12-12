from django.views.generic import TemplateView


# Create your views here.


class PermissionDeniedView(TemplateView):
    template_name = "errors/permission_denied.html"