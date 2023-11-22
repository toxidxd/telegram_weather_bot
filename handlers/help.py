from telebot.types import Message
from loader import bot
from config_data.config import DEFAULT_COMMANDS
from loguru import logger


@bot.message_handler(state="*", commands=["help"])
def bot_help(message: Message):
    logger.info(f'Send help message to {message.from_user.username}:{message.from_user.id}')
    text = [f"/{command} - {desk}" for command, desk in DEFAULT_COMMANDS]
    bot.reply_to(message, "\n".join(text))
