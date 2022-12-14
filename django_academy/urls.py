
from django.contrib import admin
from django.urls import path, include

from django_academy import exceptions as ex

handler400=ex.handle_403
handler403=ex.handle_403
handler404=ex.handle_404
handler500=ex.handle_500


urlpatterns = [
    path("admin/", admin.site.urls),
    path("auth/", include("app_user.urls")),
    path("tutor/", include("app_lecturer.urls")),
    path("course/", include("app_course.urls")),
    path("payment/", include("app_payment.urls")),
    path("", include("app_index.urls")),
]





