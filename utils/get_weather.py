from loader import bot
from telebot.types import Message
from utils.weather_request import weather_request
from utils.generate_current_message import generate_current_message
from utils.generate_forecast_message import generate_forecast_message


def current_weather(message: Message) -> None:
    print(message.text.split()[-1])
    result = weather_request(message.text.split()[-1])
    bot.send_message(message.chat.id, generate_current_message(result))


def forecast_weather(message: Message) -> None:
    print(message.text.split()[-1])
    result = weather_request(message.text.split()[-1])
    bot.send_message(message.chat.id, generate_forecast_message(result))
