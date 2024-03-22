from .views import *
from django.urls import path

urlpatterns: list = [
    path('', AccountingDCCreateView.as_view(), name='index'),
    path('get_form_payments/', get_form_payments, name='get_form_payments'),
    path('get_legal_entities/', get_legal_entities, name='get_legal_entities'),
    path('get_rcs/', get_rcs, name='get_rcs')
]
