from telebot import TeleBot
from telebot.storage import StateMemoryStorage
from config_data import config

states_storage = StateMemoryStorage()
bot = TeleBot(token=config.BOT_TOKEN, state_storage=states_storage)
