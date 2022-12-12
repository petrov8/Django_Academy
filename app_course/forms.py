from bootstrap_datepicker_plus.widgets import DateTimePickerInput

from app_course.models import CourseModel
from support.base.base_forms import BaseModelForm
from support.mixins.mixins import DisableFieldsMixin


class CourseCreateForm(BaseModelForm):
    class Meta:
        model = CourseModel
        fields = (
            "title",
            "description",
            "technology",
            "dev_type",
            "competency_level",
            "start_date",
            "price",
            "image_url"
        )

    widgets = {
        "start_date": DateTimePickerInput(),
    }


class CourseEditForm(CourseCreateForm):
    pass


class CourseDeleteForm(DisableFieldsMixin, CourseCreateForm):
    pass





