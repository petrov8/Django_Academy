from django.shortcuts import render

from app_payment.forms import CCPaymentForm
from support.add_funcs.course_support import CourseSupport
from support.add_funcs.user_support import UserSupport


def add_course_to_student(course, student):
    return course.students.add(student)


def add_student_to_course(course, student):
    course.students.add(student)
    course.participants += 1
    course.save()
    return add_course_to_student(course, student)


def cc_payment_view(request, pk):
    user = request.user
    form = CCPaymentForm(request.POST or None)
    if request.method == "POST" and UserSupport.check_if_student(user):
        if form.is_valid():
            course = CourseSupport.return_course_object(pk)
            form.instance.student_id = user.id
            form.instance.course_id = course.id
            form.save()
            add_student_to_course(course, user)
            return render(request, "courses/my-courses.html", {
                "courses": user.coursemodel_set.all()
            })
    return render(request, "payments/credit_card.html", {
        "form": form,
        "course_id": pk
    })



    # def post(self, request, *args,  **kwargs):
    #     self.object = self.get_object()
    #     user = self.request.user
    #     if UserSupport.check_if_student(user):
    #         course = self.object
    #         course.students.add(user)
    #         user.coursemodel_set.add(course)
    #         course.participants += 1
    #         course.save()
    #     return render(request, "courses/my-courses.html", {
    #         "courses": user.coursemodel_set.all()
    #     })








