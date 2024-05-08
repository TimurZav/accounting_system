import datetime
from .models import *
from typing import Dict, Optional
from .forms import AccountingDCForm
from django.http import JsonResponse
from django.db.models import QuerySet
from django.views.generic import CreateView
from django.core.handlers.wsgi import WSGIRequest


class AccountingDCCreateView(CreateView):
    model = AccountingDC
    form_class = AccountingDCForm
    template_name = "main/index.html"

    def get_context_data(self, **kwargs) -> Dict[str, QuerySet]:
        context = super().get_context_data(**kwargs)
        context['businesses'] = Business.objects.all()
        context['incoming_outgoings'] = IncomingOutgoing.objects.all()
        context['contracts'] = Contract.objects.all()
        context['clients'] = Client.objects.all()
        context['contract_numbers'] = ContractNumber.objects.all()
        context['from_clients'] = FromClient.objects.all()
        return context

    @staticmethod
    def get_related_data(request: WSGIRequest) -> JsonResponse:
        data_type = request.GET.get('data_type')
        related_id = request.GET.get('related_id')

        queryset_dict = {
            'formPayment': FormPayment.objects.filter(business_id=related_id),
            'legalEntity': LegalEntity.objects.filter(form_payment_id=related_id),
            'rc': RC.objects.filter(legal_entity_id=related_id),
            'view': View.objects.filter(incoming_outgoing_id=related_id),
            'source': Source.objects.filter(view_id=related_id),
            'group': Group.objects.filter(source_id=related_id),
            'article': Article.objects.filter(group_id=related_id),
            'additionalParams': AdditionalParams.objects.filter(article_id=related_id),
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
        base_: str = request.POST.get('base')
        rc: str = request.POST.get('rc')
        view: str = request.POST.get('view')
        contract: str = request.POST.get('contractor')
        client: str = request.POST.get('client')
        source: str = request.POST.get('source')
        article: str = request.POST.get('article')
        contract_number: str = request.POST.get('contractNumber')
        group: str = request.POST.get('group')
        additional_params: str = request.POST.get('additionalParams')
        from_client: str = request.POST.get('fromClient')
        article_additional: str = request.POST.get('articleAdditional', '')
        date_number: int = datetime.datetime.strptime(accounting_date, "%Y-%m-%d").day
        date_month: int = datetime.datetime.strptime(accounting_date, "%Y-%m-%d").month
        date_year: int = datetime.datetime.strptime(accounting_date, "%Y-%m-%d").year
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
            'base': base_,
            'view': view,
            'source': source,
            'group': group,
            'article': article,
            'additional_params': additional_params,
            'contractor': contract,
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
        incoming_outgoing_obj, _ = IncomingOutgoing.objects.get_or_create(name=incoming_outgoing)
        view_obj, _ = View.objects.get_or_create(name=view)
        source_obj, _ = Source.objects.get_or_create(name=source)
        group_obj, _ = Group.objects.get_or_create(name=group)
        article_obj, _ = Article.objects.get_or_create(name=article)
        additional_params_obj, _ = AdditionalParams.objects.get_or_create(name=additional_params)
        contract_obj, _ = Contract.objects.get_or_create(name=contract)
        client_obj, _ = Client.objects.get_or_create(name=client)
        contract_number_obj, _ = ContractNumber.objects.get_or_create(name=contract_number)
        from_client_obj, _ = FromClient.objects.get_or_create(name=from_client)

        AccountingDC.objects.create(
            business=business_obj,
            date_data_entry=date_data_entry,
            date_transaction=date_transaction,
            accounting_date=accounting_date,
            form_payment=form_payment_obj,
            incoming_outgoing=incoming_outgoing_obj,
            amount=amount,
            legal_entity=legal_entity_obj,
            rc=rc_obj,
            base=base_,
            view=view_obj,
            source=source_obj,
            group=group_obj,
            article=article_obj,
            additional_params=additional_params_obj,
            contractor=contract_obj,
            article_additional=article_additional,
            client=client_obj,
            contract_number=contract_number_obj,
            from_client=from_client_obj,
            date_number=date_number,
            date_month=date_month,
            date_year=date_year,
            amount_plan=amount_plan
        )
        return JsonResponse(response_data)
