import datetime
from typing import Dict, Optional
from .forms import AccountingDCForm
from django.http import JsonResponse
from django.db.models import QuerySet
from django.views.generic import CreateView
from django.core.handlers.wsgi import WSGIRequest
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
    def get_related_data(request: WSGIRequest) -> JsonResponse:
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

    @staticmethod
    def get_feedback(request: WSGIRequest) -> Optional[JsonResponse]:
        if request.method != 'POST':
            return

        business: str = request.POST.get('business')
        date_data_entry: datetime = datetime.datetime.now().date()
        date_transaction: str = request.POST.get('date_transaction')
        accounting_date: str = request.POST.get('accounting_date')
        form_payment: str = request.POST.get('form_payment')
        incoming_outgoing: str = request.POST.get('incoming_outgoing')
        amount: str = request.POST.get('amount')
        legal_entity: str = request.POST.get('legal_entity')
        rc: str = request.POST.get('rc')
        base: str = request.POST.get('base')
        view: str = request.POST.get('view')
        source: str = request.POST.get('source')
        group: str = request.POST.get('group')
        article: str = request.POST.get('article')
        additional_params: str = request.POST.get('additional_params')
        contractor: str = request.POST.get('contractor')
        article_additional: str = request.POST.get('article_additional')
        client: str = request.POST.get('client')
        contract_number: str = request.POST.get('contract_number')
        from_client: str = request.POST.get('from_client')
        date_number: str = request.POST.get('date_number')
        date_month: str = request.POST.get('date_month')
        date_year: str = request.POST.get('date_year')
        amount_plan: str = request.POST.get('amount_plan')

        response_data: dict = {
            'name': business,
            'date_data_entry': date_data_entry,
            'date_transaction': date_transaction,
            'accounting_date': accounting_date,
            'form_payment': form_payment,
            'incoming_outgoing': incoming_outgoing,
            'amount': amount,
            'legal_entity': legal_entity,
            'rc': rc,
            'base': base,
            'view': view,
            'source': source,
            'group': group,
            'article': article,
            'additional_params': additional_params,
            'contractor': contractor,
            'article_additional': article_additional,
            'client': client,
            'contract_number': contract_number,
            'from_client': from_client,
            'date_number': date_number,
            'date_month': date_month,
            'date_year': date_year,
            'amount_plan': amount_plan
        }

        AccountingDC.objects.create(
            date_data_entry=date_data_entry,
            date_transaction=date_transaction,
            accounting_date=accounting_date,
            form_payment=form_payment,
            incoming_outgoing=incoming_outgoing,
            amount=amount,
            legal_entity=legal_entity,
            rc=rc,
            base=base,
            view=view,
            source=source,
            group=group,
            article=article,
            additional_params=additional_params,
            contractor=contractor,
            article_additional=article_additional,
            client=client,
            contract_number=contract_number,
            from_client=from_client,
            date_number=date_number,
            date_month=date_month,
            date_year=date_year,
            amount_plan=amount_plan
        )
        return JsonResponse(response_data)
