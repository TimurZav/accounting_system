from typing import Dict
from .forms import AccountingDCForm
from django.db.models import QuerySet
from django.views.generic import CreateView
from .models import AccountingDC, Business, FormPayment, LegalEntity, RC


class AccountingDCCreateView(CreateView):
    model: AccountingDC = AccountingDC
    form_class: AccountingDCForm = AccountingDCForm
    template_name: str = "main/index.html"

    def get_context_data(self, **kwargs) -> Dict[str, QuerySet]:
        context: Dict[str, QuerySet] = super().get_context_data(**kwargs)
        context['businesses'] = Business.objects.all()
        context['form_payments'] = FormPayment.objects.all()
        context['legal_entities'] = LegalEntity.objects.all()
        context['rcs'] = RC.objects.all()
        return context
