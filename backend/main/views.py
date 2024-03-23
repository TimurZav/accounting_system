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

        date_transaction: str = request.POST.get('dateTransaction')
        business: str = request.POST.get('business')
        date_data_entry: datetime = datetime.datetime.now().date()
        accounting_date: str = request.POST.get('accountingDate')
        form_payment: str = request.POST.get('formPayment')
        amount: str = request.POST.get('amount')
        legal_entity: str = request.POST.get('legalEntity')
        incoming_outgoing: str = request.POST.get('incomingOutgoing')
        base: str = request.POST.get('base')
        rc: str = request.POST.get('rc')
        view: str = request.POST.get('view')
        contractor: str = request.POST.get('contractor')
        client: str = request.POST.get('client')
        source: str = request.POST.get('source')
        article: str = request.POST.get('article')
        contract_number: str = request.POST.get('contractNumber')
        group: str = request.POST.get('group')
        additional_params: str = request.POST.get('additionalParams')
        from_client: str = request.POST.get('fromClient')
        article_additional: str = request.POST.get('articleAdditional', '')
        date_number: str = request.POST.get('dateNumber', datetime.datetime.now().day)
        date_month: str = request.POST.get('dateMonth', datetime.datetime.now().month)
        date_year: str = request.POST.get('dateYear', datetime.datetime.now().year)
        amount_plan: str = request.POST.get('amountPlan', 2)

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

        business_obj, _ = Business.objects.get_or_create(name=business)
        form_payment_obj, _ = FormPayment.objects.get_or_create(name=form_payment)
        legal_entity_obj, _ = LegalEntity.objects.get_or_create(name=legal_entity)
        rc_obj, _ = RC.objects.get_or_create(name=rc)

        AccountingDC.objects.create(
            business=business_obj,
            date_data_entry=date_data_entry,
            date_transaction=date_transaction,
            accounting_date=accounting_date,
            form_payment=form_payment_obj,
            incoming_outgoing=incoming_outgoing,
            amount=amount,
            legal_entity=legal_entity_obj,
            rc=rc_obj,
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
