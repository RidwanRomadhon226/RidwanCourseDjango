from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def learn_django(request):
    a = '<h1>Ridwan Romadhon Django</h1>'
    return HttpResponse(a)


def learn_python(request):
    return HttpResponse('<h1>Ridwan Romadhon Python</h1>')
