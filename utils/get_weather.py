from loader import bot
from telebot.types import Message
from utils.weather_request import weather_request
from utils.generate_current_message import generate_current_message
from utils.generate_forecast_message import generate_forecast_message
from loguru import logger


def current_weather(message: Message) -> None:
    city = message.text.split()[-1]
    logger.info(f'Requesting weather in {city} from API')
    result = weather_request(city)
    logger.info(f'Send weather in {city} to {message.from_user.username}:{message.from_user.id}')
    bot.send_message(message.chat.id, generate_current_message(result))


def forecast_weather(message: Message) -> None:
    city = message.text.split()[-1]
    logger.info(f'Requesting forecast in {city} from API')
    result = weather_request(city)
    logger.info(f'Send forecast in {city} to {message.from_user.username}:{message.from_user.id}')
    bot.send_message(message.chat.id, generate_forecast_message(result))
