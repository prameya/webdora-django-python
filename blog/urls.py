# taken from poll app example
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]