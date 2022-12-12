from functools import wraps

from app_lecturer.models import LecturerModel
from app_user.models import UserProfileModel
from support.add_funcs.user_support import UserSupport


def return_profile_instance(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        user = args[0].request.user
        try:
            profile = UserProfileModel.objects.filter(user_id=user.id)[0]
            return func(profile, *args, **kwargs)
        except IndexError:
            raise IndexError("Instance doesn't exist.")
    return wrapper


def return_objects_decor(model, items):
    def wrapper_1(func):
        @wraps(func)
        def wrapper_2(*args, **kwargs):
            user = args[0].request.user
            lis = ()
            if UserSupport.check_if_student(user):
                lis = return_student_courses_data(user)
            elif UserSupport.check_if_lecturer(user):
                lis = return_lecturer_data(model, user.id, items)
            kwargs["lis"] = lis
            return func(*args, **kwargs)
        return wrapper_2
    return wrapper_1


def return_student_courses_data(student):
    a = student.coursemodel_set.all()
    return a


# used for objects in LecturerModel and CoursesModel
def return_lecturer_data(model, lecturer_id, criterion):
    if criterion == "all":
        return model.objects.filter(creator_id=lecturer_id).all()
    else:
        return model.objects.filter(creator_id=lecturer_id)[0]

