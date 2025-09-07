"""
Модели базы данных для системы управления предприятием.
"""

from peewee import (
    AutoField, CharField, IntegerField, FloatField, DateField,
    DateTimeField, BooleanField, ForeignKeyField, Model, MySQLDatabase
)


db = MySQLDatabase(
    'tree',
    user='root',
    password='root',
    host='localhost',
    port=3306,
)


class BaseModel(Model):
    """Базовая модель, к которой подключается база данных."""
    class Meta:
        '''Подключение к базе данных.'''
        database = db


class Partner(BaseModel):
    """Партнёры предприятия."""

    id = AutoField()
    type = CharField()
    name = CharField()
    adress = CharField()
    inn = CharField()
    director = CharField()
    phone = CharField()
    email = CharField()
    logo = CharField(null=True)
    reiting = IntegerField()
    sales_history = CharField(null=True)  # история реализации
    sales_places = CharField(null=True)   # места продаж


class Manager(BaseModel):
    """Менеджеры."""

    id = AutoField()
    fio = CharField()
    phone = CharField()
    email = CharField()


class Order(BaseModel):
    """Заявки."""

    id = AutoField()
    partner = ForeignKeyField(Partner, backref="orders")
    manager = ForeignKeyField(Manager, backref="orders")
    created_at = DateTimeField()
    status = CharField()
    prepayment = BooleanField(default=False)


class OrderItem(BaseModel):
    """Позиции в заявках."""

    id = AutoField()
    order = ForeignKeyField(Order, backref="items")
    product_name = CharField()
    quantity = IntegerField()
    price = FloatField()
    production_date = DateField(null=True)


class Employee(BaseModel):
    """Сотрудники."""

    id = AutoField()
    fio = CharField()
    birth_date = DateField()
    passport_data = CharField()
    bank_details = CharField()
    family_status = CharField()
    health_status = CharField()


class EquipmentAccess(BaseModel):
    """Доступ сотрудников к оборудованию."""

    id = AutoField()
    employee = ForeignKeyField(Employee, backref="access")
    equipment_name = CharField()


class AccessLog(BaseModel):
    """Журнал входа/выхода сотрудников."""

    id = AutoField()
    employee = ForeignKeyField(Employee, backref="logs")
    timestamp = DateTimeField()
    door = CharField()


class Material(BaseModel):
    """Материалы."""

    id = AutoField()
    type = CharField()
    name = CharField()
    supplier = CharField()
    pack_quantity = IntegerField()
    unit = CharField()
    description = CharField()
    image = CharField(null=True)
    cost = FloatField()
    stock_quantity = IntegerField()
    min_quantity = IntegerField()
    history = CharField(null=True)


class WarehouseOperation(BaseModel):
    """Операции на складе."""

    id = AutoField()
    material = ForeignKeyField(Material, backref="operations", null=True)
    product_name = CharField(null=True)
    type = CharField()
    quantity = IntegerField()
    date = DateTimeField()


class Supplier(BaseModel):
    """Поставщики."""

    id = AutoField()
    type = CharField()
    name = CharField()
    inn = CharField()
    delivery_history = CharField(null=True)


class Product(BaseModel):
    """Продукция."""

    id = AutoField()
    article = CharField()
    type = CharField()
    name = CharField()
    description = CharField()
    image = CharField(null=True)
    min_price = FloatField()
    weight_net = FloatField()
    weight_gross = FloatField()
    quality_cert = CharField(null=True)
    standard_number = CharField()
    price_history = CharField(null=True)
    production_time = IntegerField()
    cost_price = FloatField()
    workshop_number = CharField()
    workers_count = IntegerField()


    db.connect()
    db.create_tables([
        Partner, Manager, Order, OrderItem, Employee, EquipmentAccess,
        AccessLog, Material, WarehouseOperation, Supplier, Product,
    ])
    db.close()
