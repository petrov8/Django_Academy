import re

from django.core import exceptions


def check_if_letters_only(value):
    result = re.search(r"[^\W\d_]", value)
    if not result:
        raise exceptions.ValidationError("Name can be text only.")
    return
