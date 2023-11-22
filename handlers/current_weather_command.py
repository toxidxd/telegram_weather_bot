from utils.create_db import User
from loader import bot
from telebot.types import Message
from utils.weather_request import weather_request
from utils.generate_current_message import generate_current_message
from states.custom_states import MyStates
from loguru import logger


@bot.message_handler(state="*", commands=['weather'])
def current_weather_command(message: Message) -> None:
    user_id = message.from_user.id
    if User.get_or_none(User.user_id == user_id) is None:
        logger.info(f'Unregistered user {message.from_user.username}:{message.from_user.id}')
        bot.reply_to(message, 'Мы еще не знакомы. Введите команду /start')
        return
    else:
        logger.info(f'{message.from_user.username}:{message.from_user.id} request current weather')
        bot.set_state(message.from_user.id, MyStates.get_city_current, message.chat.id)
        print('input city')
        bot.send_message(message.chat.id, 'Введите населенный пункт')


@bot.message_handler(state=MyStates.get_city_current)
def get_current_weather(message: Message) -> None:
    city = message.text.split()[-1]
    logger.info(f'{message.from_user.username}:{message.from_user.id} gets current weather in {city}')
    result = weather_request(city)
    bot.send_message(message.chat.id, generate_current_message(result))
    bot.set_state(message.from_user.id, "*", message.chat.id)
