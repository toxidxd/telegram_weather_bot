from peewee import CharField, IntegerField, Model, SqliteDatabase
from config_data.config import BOT_DB
from loguru import logger

db = SqliteDatabase(BOT_DB)


class BaseModel(Model):
    """
    Базовый класс модели.
    """

    class Meta:
        database = db


class User(BaseModel):
    """
    Модель пользователя

    Attributes:
        user_id (int): уникальный id пользователя
        username (str): никнейм
        first_name (str): имя пользователя
        last_name (str): фамилия пользователя (может быть пустым)
    """
    user_id = IntegerField(primary_key=True)
    username = CharField(null=True)
    first_name = CharField(null=True)
    last_name = CharField(null=True)


def create_models() -> None:
    """
    Функция для создания базы данных и моделей в них
    """
    db.create_tables(BaseModel.__subclasses__())
    logger.info('Database created')
