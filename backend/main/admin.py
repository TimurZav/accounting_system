from .models import *
from django import forms
from django.db import models
from django.contrib import admin


@admin.register(Business)
class BusinessForm(admin.ModelAdmin):
    search_fields: tuple = (
        "name",
    )
    list_per_page: int = 250
    list_display: tuple = (
        "name",
    )
    formfield_overrides: dict = {
        models.CharField: {
          'widget': forms.Textarea(attrs={'rows': '4', 'cols': '50'})
        },
    }


@admin.register(FormPayment)
class FormPaymentForm(admin.ModelAdmin):
    search_fields: tuple = (
        "business",
        "name"
    )
    list_per_page: int = 250
    list_display: tuple = (
        "business",
        "name"
    )
    formfield_overrides: dict = {
        models.CharField: {
            'widget': forms.Textarea(attrs={'rows': '4', 'cols': '50'})
        },
    }


@admin.register(LegalEntity)
class LegalEntityForm(admin.ModelAdmin):
    search_fields: tuple = (
        "business",
        "form_payment",
        "name"
    )
    list_per_page: int = 250
    list_display: tuple = (
        "business",
        "form_payment",
        "name"
    )
    formfield_overrides: dict = {
        models.CharField: {
            'widget': forms.Textarea(attrs={'rows': '4', 'cols': '50'})
        },
    }


@admin.register(RC)
class RCForm(admin.ModelAdmin):
    search_fields: tuple = (
        "business",
        "form_payment",
        "legal_entity",
        "name"
    )
    list_per_page: int = 250
    list_display: tuple = (
        "business",
        "form_payment",
        "legal_entity",
        "name"
    )
    formfield_overrides: dict = {
        models.CharField: {
            'widget': forms.Textarea(attrs={'rows': '4', 'cols': '50'})
        },
    }


@admin.register(AccountingDC)
class AccountingDCForm(admin.ModelAdmin):
    search_fields: tuple = (
        "date_data_entry",
        "date_transaction",
        "business__name",
        "accounting_date",
        "form_payment__name",
        "incoming_outgoing",
        "amount",
        "legal_entity__name",
        "rc__name",
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
    )
    list_per_page: int = 250
    list_display: tuple = (
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
    )
    formfield_overrides: dict = {
        models.CharField: {
          'widget': forms.Textarea(attrs={'rows': '4', 'cols': '50'})
        },
    }
