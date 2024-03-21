from .views import *
from django.urls import path

urlpatterns: list = [
    path('', AccountingDCCreateView.as_view(), name='index'),
]
