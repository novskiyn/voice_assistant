import requests
from datetime import datetime

class WeatherService:
    def __init__(self, api_key):
        self.api_key = api_key

    def get_weather(self, city, date):
        """
        Получает прогноз погоды на указанную дату для указанного города.
        :param city: Город, для которого нужно получить прогноз.
        :param date: Дата в формате YYYY-MM-DD.
        :return: Список прогнозов погоды на указанную дату.
        """
        url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={self.api_key}&units=metric&lang=ru"
        response = requests.get(url)
        data = response.json()

        if response.status_code != 200:
            print(f"Ошибка API: {data.get('message', 'Неизвестная ошибка')}")
            return None

        if 'list' not in data:
            print("Ошибка: В ответе отсутствуют данные о погоде.")
            return None

        weather_info = []
        for forecast in data['list']:
            forecast_date = forecast['dt_txt']
            if forecast_date.startswith(date):  # Сравнение по формату YYYY-MM-DD
                weather_info.append({
                    "date": forecast_date,
                    "temperature": forecast['main']['temp'],
                    "description": forecast['weather'][0]['description']
                })

        if not weather_info:
            print(f"Нет данных о погоде в {city} на {date}.")
            return None

        return weather_info
