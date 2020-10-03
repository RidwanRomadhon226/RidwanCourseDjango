from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def fees_django(request):
    return HttpResponse('fees ridwan Romaadhon laern django')


def fees_python(request):
    return HttpResponse('fees ridwan Romaadhon laern python')
