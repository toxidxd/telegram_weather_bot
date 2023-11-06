from telebot.types import BotCommand
from config_data.config import DEFAULT_COMMANDS
from loguru import logger


def set_bot_commands(bot):
    logger.info('Setting bot commands')
    bot.set_my_commands([BotCommand(*cmd) for cmd in DEFAULT_COMMANDS])
