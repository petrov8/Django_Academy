from django.forms import Textarea
from django.utils import timezone


class SaveMixin:
    def save(self, *args, **kwargs):
        if not self.created:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(SaveMixin, self).save(*args, **kwargs)


class GetSuccessUrlMixin:
    def get_redirect_url(self):
        super().get_redirect_url()
        return self.success_url


class DisableFieldsMixin:

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__disable_fields()

    def __disable_fields(self):
        for _, field in self.fields.items():
            if isinstance(field.widget, Textarea):
                field.disabled = True
            elif field.widget.input_type == "select":
                field.disabled = True
            else:
                field.widget.attrs["readonly"] = "disable"