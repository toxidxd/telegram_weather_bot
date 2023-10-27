from loader import bot
from utils.create_db import User
from states.custom_states import MyStates
from telebot.types import Message
from utils.weather_request import weather_request
from utils.generate_forecast_message import generate_forecast_message


@bot.message_handler(state="*", commands=['forecast'])
def forecast_weather_command(message: Message) -> None:
    user_id = message.from_user.id
    if User.get_or_none(User.user_id == user_id) is None:
        bot.reply_to(message, 'Мы еще не знакомы. Введите команду /start')
        return
    else:
        bot.set_state(message.from_user.id, MyStates.get_city_forecast, message.chat.id)
        print('input city')
        bot.send_message(message.chat.id, 'Введите населенный пункт')


@bot.message_handler(state=MyStates.get_city_forecast)
def get_forecast_weather(message: Message) -> None:
    print(message.text.split()[-1])
    result = weather_request(message.text.split()[-1])
    bot.send_message(message.chat.id, generate_forecast_message(result))
    bot.set_state(message.from_user.id, "*", message.chat.id)
