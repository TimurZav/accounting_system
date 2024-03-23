from .views import *
from django.urls import path

urlpatterns: list = [
    path('', AccountingDCCreateView.as_view(), name='index'),
    path('get_related_data/', AccountingDCCreateView.get_related_data, name='get_related_data'),
    path('feedback', AccountingDCCreateView.get_feedback, name='feedback')
]
