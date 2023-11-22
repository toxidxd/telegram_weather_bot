from utils.create_db import User
from loader import bot
from telebot.types import Message
from utils.weather_request import weather_request
from utils.generate_current_message import generate_current_message
from utils.generate_forecast_message import generate_forecast_message
from loguru import logger


@bot.message_handler(state="*", content_types=['location'])
def current_weather_command(message: Message) -> None:
    user_id = message.from_user.id
    if User.get_or_none(User.user_id == user_id) is None:
        bot.reply_to(message, 'Мы еще не знакомы. Введите команду /start')
        logger.info(f'Unregistered user {message.from_user.username}:{message.from_user.id}')
        return
    else:
        user_location = f'{message.location.latitude},{message.location.longitude}'
        logger.info(f'{message.from_user.username}:{message.from_user.id} request weather '
                    f'by coordinates {user_location}')
        bot.send_message(message.chat.id, f'Ваши координаты: {user_location}')
        bot.send_message(message.chat.id, generate_current_message(weather_request(user_location)))
        bot.send_message(message.chat.id, generate_forecast_message(weather_request(user_location)))
        logger.info(f'{message.from_user.username}:{message.from_user.id} gets weather by coordinates {user_location}')

