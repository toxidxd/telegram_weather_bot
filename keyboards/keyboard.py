from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from loguru import logger


def bot_keyboard():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    b_weather = KeyboardButton("Погода")
    b_forecast = KeyboardButton("Прогноз")
    b_location = KeyboardButton("Погода по геолокации", request_location=True)
    b_help = KeyboardButton("Помощь")
    markup.add(b_weather, b_forecast, b_help, b_location)
    logger.info('Initialize bot keyboard')
    return markup
