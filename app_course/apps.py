from django.apps import AppConfig


class AppCoursesConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "app_course"

    def ready(self):
        import app_course.signals
