from django.urls import path
from . import views

urlpatterns = [
    path('leardj/', views.laern_django),
    path('learpy/', views.laern_python),
]
