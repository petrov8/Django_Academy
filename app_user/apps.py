from django.apps import AppConfig


class UserAppConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "app_user"

    def ready(self):
        import app_user.signals
        from django.db.models.signals import post_migrate

        from app_user.signals import generate_permission_groups
        post_migrate.connect(generate_permission_groups, sender=self)






