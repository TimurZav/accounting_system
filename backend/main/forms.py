from django import forms
from .models import AccountingDC, LegalEntity


class AccountingDCForm(forms.ModelForm):
    class Meta:
        model: AccountingDC = AccountingDC
        fields: list = [
            "business",
            "date_data_entry",
            "date_transaction",
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
