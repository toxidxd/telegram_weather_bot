from typing import Dict
from loguru import logger


def generate_forecast_message(json_weather: Dict) -> str:
    logger.info('Generating message with forecast')
    if 'error' not in json_weather:
        forecast = ''
        forecast += f"{json_weather['location']['name']}, прогноз погоды:\n\n"
        for i_day in json_weather['forecast']['forecastday']:
            wind_speed = round(float(i_day['day']['maxwind_kph']) // 3.6, 2)
            day_forecast = (f"{i_day['date']}\n"
                            f"Температура от {i_day['day']['mintemp_c']} C° до {i_day['day']['maxtemp_c']} C°\n"
                            f"Ветер до {wind_speed} м/с\n"
                            f"Влажность {i_day['day']['avghumidity']}%\n"
                            f"{i_day['day']['condition']['text']}\n"
                            )

            forecast += day_forecast

            if i_day['day']['daily_will_it_rain']:
                forecast += 'Возможен дождь\n'
            elif i_day['day']['daily_will_it_snow']:
                forecast += 'Возможен снег\n'
            else:
                forecast += 'Осадков не ожидается\n'
            forecast += '\n'

        return forecast
    else:
        logger.error('City is not found!')
        return 'Населенный пункт не найден!'
