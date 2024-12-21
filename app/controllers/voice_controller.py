# app/controllers/voice_controller.py
from app.services.voice_service import VoiceService
from app.controllers.reminder_controller import ReminderController
from app.controllers.note_controller import NoteController
from app.controllers.alarm_controller import AlarmController
from app.controllers.weather_controller import WeatherController
from app.controllers.coin_flip_controller import CoinFlipController

class VoiceController:
    def __init__(self):
        self.voice_service = VoiceService()
        self.reminder_controller = ReminderController()
        self.note_controller = NoteController()
        self.alarm_controller = AlarmController()
        self.weather_controller = WeatherController()
        self.coin_flip_controller = CoinFlipController()

    def recognize_speech(self):
        recognized_text = self.voice_service.recognize_speech()
        return recognized_text

    def execute_command(self, command):
        command = command.lower()  # Преобразование команды в нижний регистр
        if command.startswith("создай напоминание"):
            self.reminder_controller.create_reminder(command)
        elif command.startswith("покажи напоминание"):
            self.reminder_controller.show_reminders(command)
        elif command.startswith("отредактируй напоминание"):
            self.reminder_controller.edit_reminder(command)
        elif command.startswith("удали напоминание"):
            self.reminder_controller.delete_reminder(command)
        elif command.startswith("покажи все напоминания"):
            self.reminder_controller.show_all_reminders()
        elif command.startswith("удали все напоминания"):
            self.reminder_controller.delete_all_reminders()    
        elif command.startswith("создай заметку"):
            self.note_controller.create_note(command)
        elif command.startswith("установи будильник"):
            self.alarm_controller.set_alarm(command)
        elif command.startswith("покажи погоду"):
            self.weather_controller.get_weather()
        elif command.startswith("подбрось монетку"):
            self.coin_flip_controller.flip_coin()
        else:
            print("Неизвестная команда")

    def run(self):
        while True:
            recognized_text = self.recognize_speech()
            if recognized_text:
                print(f"Распознанный текст: {recognized_text}")
                self.execute_command(recognized_text)
