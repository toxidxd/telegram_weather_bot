from loader import bot
from utils.create_db import User
from utils.get_weather import current_weather, forecast_weather
from states.custom_states import MyStates
from config_data.config import DEFAULT_COMMANDS
from loguru import logger


@bot.message_handler(state="*", content_types=['text'])
def text_message_handler(message):
    user_id = message.from_user.id
    username = message.from_user.username
    if User.get_or_none(User.user_id == user_id) is None:
        logger.info(f'Unregistered user {message.from_user.username}:{user_id}')
        bot.reply_to(message, 'Мы еще не знакомы. Введите команду /start')
        return
    else:
        if message.text.lower() == 'погода':
            logger.info(f'{username}:{user_id} requests weather!')
            bot.set_state(message.from_user.id, MyStates.get_city_current, message.chat.id)
            bot.send_message(message.chat.id, 'Введите населенный пункт')

        elif message.text.lower() == 'прогноз':
            logger.info(f'{username}:{user_id} requests forecast!')
            bot.set_state(message.from_user.id, MyStates.get_city_forecast, message.chat.id)
            bot.send_message(message.chat.id, 'Введите населенный пункт')

        elif message.text.lower() == 'помощь':
            logger.info(f'{username}:{user_id} requests help!')
            text = [f"/{command} - {desk}" for command, desk in DEFAULT_COMMANDS]
            bot.reply_to(message, "\n".join(text))

        elif message.text.lower().startswith('погода'):
            logger.info(f'{username}:{user_id} requests weather in {message.text.split()[-1]}!')
            current_weather(message)

        elif message.text.lower().startswith('прогноз'):
            logger.info(f'{username}:{user_id} requests forecast in {message.text.split()[-1]}!')
            forecast_weather(message)

        else:
            bot.reply_to(message, 'Я Вас не понял. Введите команду /help')
