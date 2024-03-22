from typing import Dict
from .forms import AccountingDCForm
from django.http import JsonResponse
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
        return context


def get_form_payments(request):
    business_id = request.GET.get('business_id')
    form_payments = FormPayment.objects.filter(business_id=business_id)
    data = [{'value': fp.pk, 'text': fp.name} for fp in form_payments]
    return JsonResponse(data, safe=False)


def get_legal_entities(request):
    form_payment_id = request.GET.get('form_payment_id')
    legal_entities = LegalEntity.objects.filter(form_payment_id=form_payment_id)
    data = [{'value': le.pk, 'text': le.name} for le in legal_entities]
    return JsonResponse(data, safe=False)


def get_rcs(request):
    legal_entities_id = request.GET.get('legal_entities_id')
    rcs = RC.objects.filter(legal_entity_id=legal_entities_id)
    data = [{'value': rc.pk, 'text': rc.name} for rc in rcs]
    return JsonResponse(data, safe=False)
