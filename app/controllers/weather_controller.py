import re
from datetime import datetime, timedelta
from app.services.weather_service import WeatherService

class WeatherController:
    def __init__(self, api_key):
        self.weather_service = WeatherService(api_key)

    def parse_date(self, input_text):
        """
        Парсинг даты из текста на русском языке.
        Поддерживаемые форматы: "сегодня", "завтра", "25 декабря".
        Возвращает строку в формате YYYY-MM-DD или None в случае ошибки.
        """
        months = {
            "января": 1, "февраля": 2, "марта": 3, "апреля": 4, "мая": 5, "июня": 6,
            "июля": 7, "августа": 8, "сентября": 9, "октября": 10, "ноября": 11, "декабря": 12
        }

        input_text = input_text.lower().strip()

        if input_text == "сегодня":
            return datetime.now().strftime("%Y-%m-%d")

        if input_text == "завтра":
            return (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d")

        try:
            parts = input_text.split()
            if len(parts) != 2:
                raise ValueError("Некорректный формат даты. Ожидается: 'число месяц'.")

            day = int(parts[0])
            month_name = parts[1]

            if month_name not in months:
                raise ValueError(f"Некорректное название месяца: {month_name}")

            month = months[month_name]
            year = datetime.now().year

            date = datetime(year=year, month=month, day=day)
            return date.strftime("%Y-%m-%d")

        except ValueError as ve:
            print(f"Ошибка: {str(ve)}")
            return None
        except Exception as e:
            print(f"Неожиданная ошибка: {str(e)}")
            return None

    def get_weather(self, command):
        """
        Обработка команды для получения погоды.
        Ожидаемый формат команды: 'Погода (город) на (дата)'.
        """
        match = re.search(r"погода (.+?) на (.+)", command, re.IGNORECASE)
        if match:
            city = match.group(1).strip()
            date_input = match.group(2).strip()

            # Преобразование даты
            date = self.parse_date(date_input)
            if not date:
                print(f"Ошибка: Неверный формат даты '{date_input}'.")
                return

            # Запрос погоды
            weather_info = self.weather_service.get_weather(city, date)
            if weather_info:
                print(f"Погода в {city.capitalize()} на {date_input}:")
                for info in weather_info:
                    print(f"- Время: {info['date']}")
                    print(f"  Температура: {info['temperature']}°C")
                    print(f"  Описание: {info['description']}")
            else:
                print(f"Нет данных о погоде в {city.capitalize()} на {date_input}.")
        else:
            print("Неправильный формат команды. Используйте: 'Погода (город) на (дата)'.")
