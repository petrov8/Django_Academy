import re

from django.core import exceptions


def check_if_letters_and_digits_only(value):
    result = re.search(r"[^\W\d_]", value)
    if not result:
        raise exceptions.ValidationError("Input can be letters and digits only.")
    return

def check_if_letters_only(value):
    result = re.search(r"^[a-zA-Z]+(?:[\s.]+[a-zA-Z]+)*$", value)
    if not result:
        raise exceptions.ValidationError("Input can be letters only.")
    return


# def check_if_letters_and_digits_and_spaces_only(value):
#     result = re.search(r"^(?=.*[A-Za-z0-9])[A-Za-z0-9 _]*$", value)
#     if not result:
#         raise exceptions.ValidationError("Input can be letters and digits only.")
#     return
