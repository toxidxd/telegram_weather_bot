from loader import bot
from utils.create_db import User
from states.custom_states import MyStates
from telebot.types import Message
from utils.weather_request import weather_request
from utils.generate_forecast_message import generate_forecast_message
from loguru import logger


@bot.message_handler(state="*", commands=['forecast'])
def forecast_weather_command(message: Message) -> None:
    user_id = message.from_user.id
    if User.get_or_none(User.user_id == user_id) is None:
        logger.info(f'Unregistered user {message.from_user.username}:{message.from_user.id}')
        bot.reply_to(message, 'Мы еще не знакомы. Введите команду /start')
        return
    else:
        logger.info(f'{message.from_user.username} request forecast')
        bot.set_state(message.from_user.id, MyStates.get_city_forecast, message.chat.id)
        bot.send_message(message.chat.id, 'Введите населенный пункт')


@bot.message_handler(state=MyStates.get_city_forecast)
def get_forecast_weather(message: Message) -> None:
    city = message.text.split()[-1]
    result = weather_request(city)
    bot.send_message(message.chat.id, generate_forecast_message(result))
    bot.set_state(message.from_user.id, "*", message.chat.id)
    logger.info(f'{message.from_user.username} gets forecast in {city}')
