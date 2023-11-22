from typing import Dict
from loguru import logger


def generate_current_message(json_weather: Dict) -> str:
    logger.info(f'Generating message with current weather in {json_weather["location"]["name"]}')
    if 'error' not in json_weather:
        wind_speed = round(float(json_weather['current']['wind_kph'])//3.6, 2)
        wind_gusts = round(float(json_weather['current']['gust_mph'])//3.6, 2)

        my_message = (f"{json_weather['location']['name']}, погода в реальном времени:\n"
                      f"{json_weather['location']['localtime']}\n"
                      f"Температура {json_weather['current']['temp_c']} C°, "
                      f"{json_weather['current']['condition']['text']}\n"
                      f"Ощущается как {json_weather['current']['feelslike_c']} C°\n"
                      f"Ветер {wind_speed} м/с, {json_weather['current']['wind_dir']}, порывы до {wind_gusts} м/с\n"
                      f"Влажность {int(json_weather['current']['humidity'])} %\n"
                      f"Давление {int(json_weather['current']['pressure_mb'])} мм рт. ст."
                      )
        return my_message
    else:
        logger.error('City is not found!')
        return 'Населенный пункт не найден!'
