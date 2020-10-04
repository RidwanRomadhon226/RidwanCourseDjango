from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def fees_django(request):
    return HttpResponse("<h1>Hallo Fees Ridwan Romadhon Django </h1>")


def fees_python(request):
    return HttpResponse("<h1>Hallo Fees Ridwan Romadhon Python</h1>")
