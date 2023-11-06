import os
from dotenv import load_dotenv, find_dotenv
from loguru import logger


if not find_dotenv():
    logger.info('.env not found')
    exit('.env not found')
else:
    load_dotenv()


BOT_TOKEN = os.getenv("BOT_TOKEN")  # токен Telegram бота
API_KEY = os.getenv("API_KEY")  # токен доступа к API
BOT_DB = os.getenv("BOT_DB")  # путь к базе данных

# команды бота
DEFAULT_COMMANDS = (
    ("weather", "Погода сейчас"),
    ("forecast", "Прогноз погоды"),
    ("help", "Помощь")
)
