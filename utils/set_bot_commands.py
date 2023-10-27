from telebot.types import BotCommand
from config_data.config import DEFAULT_COMMANDS


def set_bot_commands(bot):
    bot.set_my_commands([BotCommand(*cmd) for cmd in DEFAULT_COMMANDS])
