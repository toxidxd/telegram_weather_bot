import handlers  # noqa
from utils.create_db import create_models
from utils.set_bot_commands import set_bot_commands
from loader import bot
from telebot.custom_filters import StateFilter
from loguru import logger
import time


def main() -> None:
    logger.add('log.log', format="{time} {level} {message}", level='INFO',
               rotation='10 KB', compression='zip')
    logger.info('Initialize bot')
    bot.add_custom_filter(StateFilter(bot))
    create_models()
    set_bot_commands(bot)
    try:
        bot.infinity_polling()
    except Exception as ex:
        print(ex)
        time.sleep(10)


if __name__ == '__main__':
    main()

