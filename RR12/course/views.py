from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def learn_django(request):
    nama = 'Ridwan'
    umur = 24
    Pekerjaan = 'Web Dev'
    coursename = {'nm': nama, 'um': umur, 'job': Pekerjaan}
    return render(request, 'course/courseone.html', coursename)


def learn_python(request):
    return render(request, 'course/coursetow.html')
