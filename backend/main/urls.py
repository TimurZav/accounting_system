from django.urls import path
from .views import *

urlpatterns: list = [
    path('', IndexView.as_view(), name='index'),
]
