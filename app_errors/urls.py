from django.urls import path, include



import app_errors.views as resource

urlpatterns = [
    path("new/", resource.PermissionDeniedView.as_view(), name="permission denied"),
]
