# app/controllers/weather_controller.py
class WeatherController:
    def get_weather(self):
        # Вывод информации о погоде
        weather = {
            "temperature": 10,
            "condition": "Солнечно"
        }
        print(f"Температура: {weather['temperature']}°C, Условия: {weather['condition']}")
