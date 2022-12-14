from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.template.response import TemplateResponse


def handler404(request, *args, **kwargs):

    template = loader.get_template("exceptions/404_user_not_found.html")
    return TemplateResponse(template.render(request), status=404)