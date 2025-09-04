from peewee import MySQLDatabase, Model, AutoField, IntegerField, CharField, \
    DateField, DateTimeField, ForeignKeyField

db = MySQLDatabase(
    'tree',
    user='root',
    password='root',
    host='localhost',
    port=3306
)

class BaseModel(Model):
    """Базовая модель"""

    class Meta:
        """Класс мета"""
        database = db


class Partners(BaseModel):
    ''' Партнеры '''
    id = AutoField()
    type = CharField()
    name = CharField()
    adress = CharField()
    inn = IntegerField()
    director = CharField()
    phone = IntegerField()
    email = CharField()
    logo = CharField()
    reiting = IntegerField()

db.connect()
db.create_tables([Partners])
db.close()
