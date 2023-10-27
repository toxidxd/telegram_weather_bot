from loader import bot
from utils.create_db import User
from utils.get_weather import current_weather, forecast_weather
from states.custom_states import MyStates
from config_data.config import DEFAULT_COMMANDS


@bot.message_handler(state="*", content_types=['text'])
def text_message_handler(message):
    user_id = message.from_user.id
    if User.get_or_none(User.user_id == user_id) is None:
        bot.reply_to(message, 'Мы еще не знакомы. Введите команду /start')
        return
    else:
        if message.text.lower() == 'погода':
            bot.set_state(message.from_user.id, MyStates.get_city_current, message.chat.id)
            print('input city')
            bot.send_message(message.chat.id, 'Введите населенный пункт')

        elif message.text.lower() == 'прогноз':
            bot.set_state(message.from_user.id, MyStates.get_city_forecast, message.chat.id)
            print('input city')
            bot.send_message(message.chat.id, 'Введите населенный пункт')

        elif message.text.lower() == 'помощь':
            text = [f"/{command} - {desk}" for command, desk in DEFAULT_COMMANDS]
            bot.reply_to(message, "\n".join(text))

        elif message.text.lower().startswith('погода'):
            current_weather(message)

        elif message.text.lower().startswith('прогноз'):
            forecast_weather(message)

        else:
            bot.reply_to(message, 'Я Вас не понял. Введите команду /help')
