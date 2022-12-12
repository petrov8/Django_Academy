

class CommonSupport:

    @staticmethod
    def check_forms_validity(*args):
        valid = True

        for form in args:
            if form and not form.is_valid():
                valid = False

        return valid