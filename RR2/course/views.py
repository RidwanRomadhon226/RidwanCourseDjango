from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(requesr):
    return HttpResponse('Home Page')


def learn_django(request):
    return HttpResponse('Hallo Ridwan')


def learn_python(request):
    return HttpResponse('<h1>Hallo Ridwan Learn Pthon</h1>')


def learn_var(request):
    a = '<h1>Hallo Ridwan</h1>'
    return HttpResponse(a)


def learn_math(request):
    a = 10 + 10
    return HttpResponse(a)


def learn_format(request):
    a = 'Ridwan Romadhon'
    return HttpResponse(f'Halo {a}')
