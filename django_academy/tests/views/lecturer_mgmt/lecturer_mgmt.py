from django_academy.tests.base import BaseTestClass

sample_profile_pic = "https://cdn.pixabay.com/photo/2016/12/14/03/08/raccoon-1905528__340.jpg"


class BaseLecturerUser(BaseTestClass):

    lecturer_details = {
        "first_name": "Test",
        "last_name": "Testing",
        "age": 21,
        "gender": "Male",
        "profile_picture": sample_profile_pic,
        "years_of_experience": 10,
        "fav_language": "Python",
        "about_me": "This is a big testcase eheheheheh",

    }


