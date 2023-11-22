from loader import bot
from telebot.types import Message
from peewee import IntegrityError
from utils.create_db import User
from keyboards.keyboard import bot_keyboard
from loguru import logger


@bot.message_handler(state="*", commands=['start'])
def start(message: Message) -> None:
    """
    Функция для команды /start. Приветствует пользователя и регистрирует его в базе данных.
    :param message:
    """
    user_id = message.from_user.id
    username = message.from_user.username
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name

    try:
        User.create(
            user_id=user_id,
            username=username,
            first_name=first_name,
            last_name=last_name
        )
        bot.send_message(user_id, f'Привет, {username} (id:{user_id})!', reply_markup=bot_keyboard())
        logger.info(f'{username}:{user_id} was registered!')

    except IntegrityError:
        logger.info(f'{username}:{user_id} try register again!')
        bot.send_message(user_id, f'И снова привет, {username} (id:{user_id})!')

