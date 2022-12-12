from django.urls import path, include
import app_payment.views as resource


urlpatterns = [
    path("<int:pk>/", include([
        path("", resource.cc_payment_view, name="payment"),
    ]))
]

