from django.db.models import *
from smart_selects.db_fields import ChainedForeignKey


class Business(Model):
    name: CharField = CharField(blank=False, verbose_name='Бизнес')

    def __str__(self):
        return self.name

    class Meta:
        managed: bool = True
        db_table: str = 'business'
        verbose_name_plural: str = 'Бизнес'


class FormPayment(Model):
    business = ForeignKey(Business, on_delete=SET_NULL, null=True, verbose_name="Бизнес")
    name = CharField(blank=False, verbose_name="Форма оплаты")

    def __str__(self):
        return self.name

    class Meta:
        managed: bool = True
        db_table: str = 'form_payment'
        verbose_name_plural: str = 'Форма оплаты'


class LegalEntity(Model):
    business = ForeignKey(Business, on_delete=SET_NULL, null=True, verbose_name="Бизнес")
    form_payment = ForeignKey(FormPayment, on_delete=SET_NULL, null=True, verbose_name="Форма оплаты")
    name: CharField = CharField(blank=False, verbose_name="Юр. лицо")

    def __str__(self):
        return self.name

    class Meta:
        managed: bool = True
        db_table: str = 'legal_entity'
        verbose_name_plural: str = 'Юр. лицо'


class RC(Model):
    business = ForeignKey(Business, on_delete=SET_NULL, null=True, verbose_name="Бизнес")
    form_payment = ForeignKey(FormPayment, on_delete=SET_NULL, null=True, verbose_name="Форма оплаты")
    legal_entity = ForeignKey(LegalEntity, on_delete=SET_NULL, null=True, verbose_name="Юр. лицо")
    name: CharField = CharField(blank=False, verbose_name="Р/с")

    def __str__(self):
        return self.name

    class Meta:
        managed: bool = True
        db_table: str = 'rc'
        verbose_name_plural: str = 'Р/с'


class AccountingDC(Model):
    business: ForeignKey = ForeignKey(Business, on_delete=SET_NULL, null=True, verbose_name='Бизнес')
    date_data_entry: DateField = DateField(blank=False, verbose_name='Дата ввода данных')
    date_transaction: DateField = DateField(blank=True, verbose_name='Дата транзакции')
    accounting_date: DateField = DateField(blank=False, verbose_name='Дата учета')
    form_payment: ChainedForeignKey = ChainedForeignKey(
        FormPayment,
        chained_field="business",
        chained_model_field="business",
        verbose_name="Форма платежа",
        show_all=False,
        auto_choose=True,
        sort=True
    )
    incoming_outgoing: CharField = CharField(blank=True, verbose_name='Приход/Расход')
    amount: FloatField = FloatField(blank=True, verbose_name='Сумма')
    legal_entity: ChainedForeignKey = ChainedForeignKey(
        LegalEntity,
        chained_field="form_payment",
        chained_model_field="form_payment",
        verbose_name="Юр. лицо",
        show_all=False,
        auto_choose=True,
        sort=True
    )
    rc: ChainedForeignKey = ChainedForeignKey(
        RC,
        chained_field="legal_entity",
        chained_model_field="legal_entity",
        verbose_name="Р/с",
        show_all=False,
        auto_choose=True,
        sort=True
    )
    base: CharField = CharField(blank=True, verbose_name='Основание')
    view: CharField = CharField(blank=True, verbose_name='Вид')
    source: CharField = CharField(blank=True, verbose_name='Источник')
    group: CharField = CharField(blank=True, verbose_name='Группа')
    article: CharField = CharField(blank=True, verbose_name='Статья')
    additional_params: CharField = CharField(blank=True, verbose_name='Доп параметры')
    contractor: CharField = CharField(blank=True, verbose_name='Контрагент')
    article_additional: CharField = CharField(blank=True, verbose_name='Статья+Доп')
    client: CharField = CharField(blank=True, verbose_name='Клиент')
    contract_number: CharField = CharField(blank=True, verbose_name='Номер договора')
    from_client: CharField = CharField(blank=True, verbose_name='Откуда клиент')
    date_number: IntegerField = IntegerField(blank=True, verbose_name='Число')
    date_month: IntegerField = IntegerField(blank=True, verbose_name='Месяц')
    date_year: IntegerField = IntegerField(blank=True, verbose_name='Год')
    amount_plan: FloatField = FloatField(blank=True, verbose_name='Сумма план')

    def __str__(self):
        return self.contract_number

    class Meta:
        managed: bool = True
        db_table: str = 'accounting_dc'
        verbose_name_plural: str = 'Учёт ДС'
