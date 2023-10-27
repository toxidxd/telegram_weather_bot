import handlers  # noqa
from utils.create_db import create_models
from utils.set_bot_commands import set_bot_commands
from loader import bot
from telebot.custom_filters import StateFilter


def main() -> None:
    bot.add_custom_filter(StateFilter(bot))
    create_models()
    set_bot_commands(bot)
    bot.infinity_polling()


if __name__ == '__main__':
    main()
