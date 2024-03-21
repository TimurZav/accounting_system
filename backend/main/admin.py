from .models import *
from django import forms
from django.db import models
from django.contrib import admin


@admin.register(Business)
class BusinessForm(admin.ModelAdmin):
    search_fields: list = [
        "name"
    ]
    list_per_page: int = 250
    list_display: list = [
        "name"
    ]
    formfield_overrides: dict = {
        models.CharField: {
          'widget': forms.Textarea(attrs={'rows': '4', 'cols': '50'})
        },
    }


@admin.register(FormPayment)
class FormPaymentForm(admin.ModelAdmin):
    search_fields: list = [
        "business",
        "form_payment"
    ]
    list_per_page: int = 250
    list_display: list = [
        "business",
        "form_payment"
    ]
    formfield_overrides: dict = {
        models.CharField: {
            'widget': forms.Textarea(attrs={'rows': '4', 'cols': '50'})
        },
    }


@admin.register(LegalEntity)
class LegalEntityForm(admin.ModelAdmin):
    search_fields: list = [
        "business",
        "form_payment",
        "legal_entity"
    ]
    list_per_page: int = 250
    list_display: list = [
        "business",
        "form_payment",
        "legal_entity"
    ]
    formfield_overrides: dict = {
        models.CharField: {
            'widget': forms.Textarea(attrs={'rows': '4', 'cols': '50'})
        },
    }


@admin.register(RC)
class RCForm(admin.ModelAdmin):
    search_fields: list = [
        "business",
        "form_payment",
        "legal_entity",
        "rc"
    ]
    list_per_page: int = 250
    list_display: list = [
        "business",
        "form_payment",
        "legal_entity",
        "rc"
    ]
    formfield_overrides: dict = {
        models.CharField: {
            'widget': forms.Textarea(attrs={'rows': '4', 'cols': '50'})
        },
    }


@admin.register(AccountingDC)
class AccountingDCForm(admin.ModelAdmin):
    search_fields: list = [
        "date_data_entry",
        "date_transaction",
        "business",
        "accounting_date",
        "form_payment",
        "incoming_outgoing",
        "amount",
        "legal_entity",
        "rc",
        "base",
        "view",
        "source",
        "group",
        "article",
        "additional_params",
        "contractor",
        "article_additional",
        "client",
        "contract_number",
        "from_client",
        "date_number",
        "date_month",
        "date_year",
        "amount_plan"
    ]
    list_per_page: int = 250
    list_display: list = [
        "date_data_entry",
        "date_transaction",
        "business",
        "accounting_date",
        "form_payment",
        "incoming_outgoing",
        "amount",
        "legal_entity",
        "rc",
        "base",
        "view",
        "source",
        "group",
        "article",
        "additional_params",
        "contractor",
        "article_additional",
        "client",
        "contract_number",
        "from_client",
        "date_number",
        "date_month",
        "date_year",
        "amount_plan"
    ]
    formfield_overrides: dict = {
        models.CharField: {
          'widget': forms.Textarea(attrs={'rows': '4', 'cols': '50'})
        },
    }