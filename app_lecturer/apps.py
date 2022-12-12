from django.apps import AppConfig


class AppLecturerConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "app_lecturer"

    def ready(self):
        import app_lecturer.signals
