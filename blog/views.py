from django.shortcuts import render

# taken from poll app example
from django.http import HttpResponse

# import from blog app
from blog.models import BlogPost

def index(request):
    return HttpResponse("Hello, world. You're at the blog index.")


def post(request, id):
    return HttpResponse("You're looking at blog %s." % id)

def category(request, id):
    response = "You're looking at the results of category %s."
    return HttpResponse(response % id)

def tag(request, id):
    return HttpResponse("You're voting on tag %s." % id)