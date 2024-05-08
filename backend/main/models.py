from django.db.models import *
from smart_selects.db_fields import ChainedForeignKey


# Financial data


class Business(Model):
    name: CharField = CharField(blank=False, verbose_name='Бизнес')

    def __str__(self):
        return self.name

    class Meta:
        managed: bool = True
        db_table: str = 'business'
        verbose_name_plural: str = 'Бизнес'


class FormPayment(Model):
    business: ForeignKey = ForeignKey(Business, on_delete=SET_NULL, null=True, verbose_name="Бизнес")
    name: CharField = CharField(blank=False, verbose_name="Форма оплаты")

    def __str__(self):
        return self.name

    class Meta:
        managed: bool = True
        db_table: str = 'form_payment'
        verbose_name_plural: str = 'Форма оплаты'


class LegalEntity(Model):
    business: ForeignKey = ForeignKey(Business, on_delete=SET_NULL, null=True, verbose_name="Бизнес")
    form_payment: ForeignKey = ForeignKey(FormPayment, on_delete=SET_NULL, null=True, verbose_name="Форма оплаты")
    name: CharField = CharField(blank=False, verbose_name="Юр. лицо")

    def __str__(self):
        return self.name

    class Meta:
        managed: bool = True
        db_table: str = 'legal_entity'
        verbose_name_plural: str = 'Юр. лицо'


class RC(Model):
    business: ForeignKey = ForeignKey(Business, on_delete=SET_NULL, null=True, verbose_name="Бизнес")
    form_payment: ForeignKey = ForeignKey(FormPayment, on_delete=SET_NULL, null=True, verbose_name="Форма оплаты")
    legal_entity: ForeignKey = ForeignKey(LegalEntity, on_delete=SET_NULL, null=True, verbose_name="Юр. лицо")
    name: CharField = CharField(blank=False, verbose_name="Р/с")

    def __str__(self):
        return self.name

    class Meta:
        managed: bool = True
        db_table: str = 'rc'
        verbose_name_plural: str = 'Р/с'


# Accounting data


class IncomingOutgoing(Model):
    name: CharField = CharField(blank=False, verbose_name='Приход/Расход')

    def __str__(self):
        return self.name

    class Meta:
        managed: bool = True
        db_table: str = 'incoming_outgoing'
        verbose_name_plural: str = 'Приход/Расход'


class View(Model):
    incoming_outgoing: ForeignKey = ForeignKey(IncomingOutgoing, on_delete=SET_NULL, null=True,
                                               verbose_name='Приход/Расход')
    name: CharField = CharField(blank=False, verbose_name='Вид')

    def __str__(self):
        return self.name

    class Meta:
        managed: bool = True
        db_table: str = 'view'
        verbose_name_plural: str = 'Вид'


class Source(Model):
    incoming_outgoing: ForeignKey = ForeignKey(IncomingOutgoing, on_delete=SET_NULL, null=True,
                                               verbose_name="Приход/Расход")
    view: ForeignKey = ForeignKey(View, on_delete=SET_NULL, null=True, verbose_name="Вид")
    name: CharField = CharField(blank=False, verbose_name='Источник')

    def __str__(self):
        return self.name

    class Meta:
        managed: bool = True
        db_table: str = 'source'
        verbose_name_plural: str = 'Источник'


class Group(Model):
    incoming_outgoing: ForeignKey = ForeignKey(IncomingOutgoing, on_delete=SET_NULL, null=True,
                                               verbose_name='Приход/Расход')
    view: ForeignKey = ForeignKey(View, on_delete=SET_NULL, null=True, verbose_name='Вид')
    source: ForeignKey = ForeignKey(Source, on_delete=SET_NULL, null=True, verbose_name='Источник')
    name: CharField = CharField(blank=False, verbose_name='Группа')

    def __str__(self):
        return self.name

    class Meta:
        managed: bool = True
        db_table: str = 'group'
        verbose_name_plural: str = 'Группа'


class Article(Model):
    incoming_outgoing: ForeignKey = ForeignKey(IncomingOutgoing, on_delete=SET_NULL, null=True,
                                               verbose_name='Приход/Расход')
    view: ForeignKey = ForeignKey(View, on_delete=SET_NULL, null=True, verbose_name='Вид')
    source: ForeignKey = ForeignKey(Source, on_delete=SET_NULL, null=True, verbose_name='Источник')
    group: ForeignKey = ForeignKey(Group, on_delete=SET_NULL, null=True, verbose_name='Группа')
    name: CharField = CharField(blank=False, verbose_name='Статья')

    def __str__(self):
        return self.name

    class Meta:
        managed: bool = True
        db_table: str = 'article'
        verbose_name_plural: str = 'Статья'


class AdditionalParams(Model):
    incoming_outgoing: ForeignKey = ForeignKey(IncomingOutgoing, on_delete=SET_NULL, null=True,
                                               verbose_name='Приход/Расход')
    view: ForeignKey = ForeignKey(View, on_delete=SET_NULL, null=True, verbose_name='Вид')
    source: ForeignKey = ForeignKey(Source, on_delete=SET_NULL, null=True, verbose_name='Источник')
    group: ForeignKey = ForeignKey(Group, on_delete=SET_NULL, null=True, verbose_name='Группа')
    article: ForeignKey = ForeignKey(Article, on_delete=SET_NULL, null=True, verbose_name='Статья')
    name: CharField = CharField(blank=False, verbose_name='Доп параметры')

    def __str__(self):
        return self.name

    class Meta:
        managed: bool = True
        db_table: str = 'additional_params'
        verbose_name_plural: str = 'Доп параметры'


# Single accounting table


class Contract(Model):
    name: CharField = CharField(blank=False, verbose_name='Контрагент')

    def __str__(self):
        return self.name

    class Meta:
        managed: bool = True
        db_table: str = 'contract'
        verbose_name_plural: str = 'Контрагент'


class Client(Model):
    name: CharField = CharField(blank=False, verbose_name='Клиент')

    def __str__(self):
        return self.name

    class Meta:
        managed: bool = True
        db_table: str = 'client'
        verbose_name_plural: str = 'Клиент'


class ContractNumber(Model):
    name: CharField = CharField(blank=False, verbose_name='Номер договора')

    def __str__(self):
        return self.name

    class Meta:
        managed: bool = True
        db_table: str = 'contract_number'
        verbose_name_plural: str = 'Номер договора'


class FromClient(Model):
    name: CharField = CharField(blank=False, verbose_name='Откуда клиент')

    def __str__(self):
        return self.name

    class Meta:
        managed: bool = True
        db_table: str = 'from_client'
        verbose_name_plural: str = 'Откуда клиент'


# Form for accounting data


class AccountingDC(Model):
    business: ForeignKey = ForeignKey(Business, on_delete=SET_NULL, null=True, verbose_name='Бизнес')
    date_data_entry: DateField = DateField(blank=False, verbose_name='Дата ввода данных', null=True)
    date_transaction: DateField = DateField(blank=True, verbose_name='Дата транзакции')
    accounting_date: DateField = DateField(blank=False, verbose_name='Дата учета')
    form_payment: ChainedForeignKey = ChainedForeignKey(
        FormPayment,
        chained_field="business",
        chained_model_field="business",
        verbose_name="Форма платежа",
        show_all=False,
        auto_choose=True,
        sort=True,
        null=True
    )
    incoming_outgoing: ForeignKey = ForeignKey(IncomingOutgoing, on_delete=SET_NULL, null=True,
                                               verbose_name='Приход/Расход')
    amount: FloatField = FloatField(blank=True, verbose_name='Сумма')
    legal_entity: ChainedForeignKey = ChainedForeignKey(
        LegalEntity,
        chained_field="form_payment",
        chained_model_field="form_payment",
        verbose_name="Юр. лицо",
        show_all=False,
        auto_choose=True,
        sort=True,
        null=True
    )
    rc: ChainedForeignKey = ChainedForeignKey(
        RC,
        chained_field="legal_entity",
        chained_model_field="legal_entity",
        verbose_name="Р/с",
        show_all=False,
        auto_choose=True,
        sort=True,
        null=True
    )
    base: CharField = CharField(blank=True, verbose_name='Основание')
    view: ChainedForeignKey = ChainedForeignKey(
        View,
        chained_field="incoming_outgoing",
        chained_model_field="incoming_outgoing",
        verbose_name="Вид",
        show_all=False,
        auto_choose=True,
        sort=True,
        null=True
    )
    source: ChainedForeignKey = ChainedForeignKey(
        Source,
        chained_field="view",
        chained_model_field="view",
        verbose_name="Источник",
        show_all=False,
        auto_choose=True,
        sort=True,
        null=True
    )
    group: ChainedForeignKey = ChainedForeignKey(
        Group,
        chained_field="source",
        chained_model_field="source",
        verbose_name="Группа",
        show_all=False,
        auto_choose=True,
        sort=True,
        null=True
    )
    article: ChainedForeignKey = ChainedForeignKey(
        Article,
        chained_field="group",
        chained_model_field="group",
        verbose_name="Статья",
        show_all=False,
        auto_choose=True,
        sort=True,
        null=True
    )
    additional_params: ChainedForeignKey = ChainedForeignKey(
        AdditionalParams,
        chained_field="article",
        chained_model_field="article",
        verbose_name="Доп параметры",
        show_all=False,
        auto_choose=True,
        sort=True,
        null=True
    )
    contractor: ForeignKey = ForeignKey(Contract, on_delete=SET_NULL, null=True, verbose_name='Контрагент')
    article_additional: CharField = CharField(blank=True, verbose_name='Статья+Доп', null=True)
    client: ForeignKey = ForeignKey(Client, on_delete=SET_NULL, null=True, verbose_name='Клиент')
    contract_number: ForeignKey = ForeignKey(ContractNumber, on_delete=SET_NULL, null=True,
                                             verbose_name='Номер договора')
    from_client: ForeignKey = ForeignKey(FromClient, on_delete=SET_NULL, null=True, verbose_name='Откуда клиент')
    date_number: IntegerField = IntegerField(blank=True, verbose_name='Число')
    date_month: IntegerField = IntegerField(blank=True, verbose_name='Месяц')
    date_year: IntegerField = IntegerField(blank=True, verbose_name='Год')
    amount_plan: FloatField = FloatField(blank=True, verbose_name='Сумма план', null=True)

    def __str__(self):
        return self.contract_number

    class Meta:
        managed: bool = True
        db_table: str = 'accounting_dc'
        verbose_name_plural: str = 'Учёт ДС'
