from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def learn_django():
    return HttpResponse("<h1>Hallo Ridwan Romadhon Django </h1>")


def learn_python():
    return HttpResponse("<h1>Hallo Ridwan Romadhon Python</h1>")
