from typing import Dict
from .forms import AccountingDCForm
from django.http import JsonResponse
from django.db.models import QuerySet
from django.views.generic import CreateView
from .models import AccountingDC, Business, FormPayment, LegalEntity, RC


class AccountingDCCreateView(CreateView):
    model = AccountingDC
    form_class = AccountingDCForm
    template_name = "main/index.html"

    def get_context_data(self, **kwargs) -> Dict[str, QuerySet]:
        context = super().get_context_data(**kwargs)
        context['businesses'] = Business.objects.all()
        return context

    @staticmethod
    def get_related_data(request):
        data_type = request.GET.get('data_type')
        related_id = request.GET.get('related_id')

        queryset_dict = {
            'formPayment': FormPayment.objects.filter(business_id=related_id),
            'legalEntity': LegalEntity.objects.filter(form_payment_id=related_id),
            'rc': RC.objects.filter(legal_entity_id=related_id),
        }

        queryset = queryset_dict.get(data_type)
        if queryset is None:
            return JsonResponse({'error': 'Invalid data type'}, status=400)

        data = [{'value': item.pk, 'text': item.name} for item in queryset]
        return JsonResponse(data, safe=False)
