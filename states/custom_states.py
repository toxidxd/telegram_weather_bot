from telebot.handler_backends import StatesGroup, State


class MyStates(StatesGroup):
    get_city_current = State()
    get_city_forecast = State()
