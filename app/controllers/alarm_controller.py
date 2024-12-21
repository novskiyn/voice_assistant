# app/controllers/alarm_controller.py
class AlarmController:
    def set_alarm(self, time):
        # Установка будильника
        alarm = {
            "time": time,
            "date": "2024-12-20"
        }
        # Сохранение будильника в базе данных
        print(f"Будильник установлен на {alarm['time']}")
