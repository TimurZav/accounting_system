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
    tuple_data: tuple = (
        "business",
        "name"
    )
    search_fields: tuple = tuple_data
    list_per_page: int = 250
    list_display: tuple = tuple_data
    formfield_overrides: dict = {
        models.CharField: {
            'widget': forms.Textarea(attrs={'rows': '4', 'cols': '50'})
        },
    }


@admin.register(LegalEntity)
class LegalEntityForm(admin.ModelAdmin):
    tuple_data: tuple = (
        "business",
        "form_payment",
        "name"
    )
    search_fields: tuple = tuple_data
    list_per_page: int = 250
    list_display: tuple = tuple_data
    formfield_overrides: dict = {
        models.CharField: {
            'widget': forms.Textarea(attrs={'rows': '4', 'cols': '50'})
        },
    }


@admin.register(RC)
class RCForm(admin.ModelAdmin):
    tuple_data: tuple = (
        "business",
        "form_payment",
        "legal_entity",
        "name"
    )
    search_fields: tuple = tuple_data
    list_per_page: int = 250
    list_display: tuple = tuple_data
    formfield_overrides: dict = {
        models.CharField: {
            'widget': forms.Textarea(attrs={'rows': '4', 'cols': '50'})
        },
    }


@admin.register(IncomingOutgoing)
class IncomingOutgoingForm(admin.ModelAdmin):
    tuple_data: tuple = (
        "name",
    )
    search_fields: tuple = tuple_data
    list_per_page: int = 250
    list_display: tuple = tuple_data
    formfield_overrides: dict = {
        models.CharField: {
            'widget': forms.Textarea(attrs={'rows': '4', 'cols': '50'})
        },
    }


@admin.register(View)
class ViewForm(admin.ModelAdmin):
    tuple_data: tuple = (
        "incoming_outgoing",
        "name",
    )
    search_fields: tuple = tuple_data
    list_per_page: int = 250
    list_display: tuple = tuple_data
    formfield_overrides: dict = {
        models.CharField: {
            'widget': forms.Textarea(attrs={'rows': '4', 'cols': '50'})
        },
    }


@admin.register(Source)
class SourceForm(admin.ModelAdmin):
    tuple_data: tuple = (
        "incoming_outgoing",
        "view",
        "name",
    )
    search_fields: tuple = tuple_data
    list_per_page: int = 250
    list_display: tuple = tuple_data
    formfield_overrides: dict = {
        models.CharField: {
            'widget': forms.Textarea(attrs={'rows': '4', 'cols': '50'})
        },
    }


@admin.register(Group)
class GroupForm(admin.ModelAdmin):
    tuple_data: tuple = (
        "incoming_outgoing",
        "view",
        "source",
        "name",
    )
    search_fields: tuple = tuple_data
    list_per_page: int = 250
    list_display: tuple = tuple_data
    formfield_overrides: dict = {
        models.CharField: {
            'widget': forms.Textarea(attrs={'rows': '4', 'cols': '50'})
        },
    }


@admin.register(Article)
class ArticleForm(admin.ModelAdmin):
    tuple_data: tuple = (
        "incoming_outgoing",
        "view",
        "source",
        "group",
        "name",
    )
    search_fields: tuple = tuple_data
    list_per_page: int = 250
    list_display: tuple = tuple_data
    formfield_overrides: dict = {
        models.CharField: {
            'widget': forms.Textarea(attrs={'rows': '4', 'cols': '50'})
        },
    }


@admin.register(AdditionalParams)
class AdditionalParamsForm(admin.ModelAdmin):
    tuple_data: tuple = (
        "incoming_outgoing",
        "view",
        "source",
        "group",
        "article",
        "name",
    )
    search_fields: tuple = tuple_data
    list_per_page: int = 250
    list_display: tuple = tuple_data
    formfield_overrides: dict = {
        models.CharField: {
            'widget': forms.Textarea(attrs={'rows': '4', 'cols': '50'})
        },
    }


@admin.register(Contract)
class ContractorForm(admin.ModelAdmin):
    tuple_data: tuple = (
        "name",
    )
    search_fields: tuple = tuple_data
    list_per_page: int = 250
    list_display: tuple = tuple_data
    formfield_overrides: dict = {
        models.CharField: {
            'widget': forms.Textarea(attrs={'rows': '4', 'cols': '50'})
        },
    }


@admin.register(Client)
class ClientForm(admin.ModelAdmin):
    tuple_data: tuple = (
        "name",
    )
    search_fields: tuple = tuple_data
    list_per_page: int = 250
    list_display: tuple = tuple_data
    formfield_overrides: dict = {
        models.CharField: {
            'widget': forms.Textarea(attrs={'rows': '4', 'cols': '50'})
        },
    }


@admin.register(ContractNumber)
class ContractNumberForm(admin.ModelAdmin):
    tuple_data: tuple = (
        "name",
    )
    search_fields: tuple = tuple_data
    list_per_page: int = 250
    list_display: tuple = tuple_data
    formfield_overrides: dict = {
        models.CharField: {
            'widget': forms.Textarea(attrs={'rows': '4', 'cols': '50'})
        },
    }


@admin.register(FromClient)
class FromClientForm(admin.ModelAdmin):
    tuple_data: tuple = (
        "name",
    )
    search_fields: tuple = tuple_data
    list_per_page: int = 250
    list_display: tuple = tuple_data
    formfield_overrides: dict = {
        models.CharField: {
            'widget': forms.Textarea(attrs={'rows': '4', 'cols': '50'})
        },
    }


@admin.register(AccountingDC)
class AccountingDCForm(admin.ModelAdmin):
    tuple_data: tuple = (
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
    search_fields: tuple = tuple_data
    list_per_page: int = 250
    list_filter: tuple = ('date_data_entry', 'date_transaction', 'business__name')
    list_display: tuple = tuple_data
    formfield_overrides: dict = {
        models.CharField: {
          'widget': forms.Textarea(attrs={'rows': '4', 'cols': '50'})
        },
    }
