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
        self.weather_controller = WeatherController("8ef7299116a6a9503a3ff014b32b9cc2")
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
        elif command.startswith("покажи заметку"):
            self.note_controller.show_notes(command)
        elif command.startswith("отредактируй заметку"):
            self.note_controller.edit_note(command)
        elif command.startswith("удали заметку"):
            self.note_controller.delete_note(command)
        elif command.startswith("удали пункт"):
            self.note_controller.delete_point(command)
        elif command.startswith("покажи все заметки"):
            self.note_controller.show_all_notes()
        elif command.startswith("установи будильник"):
            self.alarm_controller.set_alarm(command)
        elif command.startswith("погода"):
            self.weather_controller.get_weather(command)
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
