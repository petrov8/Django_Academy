from app_lecturer.models import LecturerModel
from support.base.base_forms import BaseModelForm


class LecturerRegisterForm(BaseModelForm):
    class Meta:
        model = LecturerModel
        fields = (
            "years_of_experience",
            "fav_language",
            "about_me",
        )


class LecturerEditForm(LecturerRegisterForm):
    pass
