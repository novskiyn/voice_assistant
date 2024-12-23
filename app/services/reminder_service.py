from app.models.reminder_model import ReminderModel

class ReminderService:
    def __init__(self):
        self.reminder_model = ReminderModel()

    def create_reminder(self, text, date):
        # Создание напоминания
        reminder = {
            "text": text,
            "date": date
        }
        # Сохранение напоминания в базе данных
        self.reminder_model.save_reminder(reminder)
        print(f"Напоминание создано: {reminder['text']}")

    def edit_reminder(self, old_text, old_date, new_text):
        # Редактирование напоминания
        self.reminder_model.edit_reminder(old_text, old_date, new_text)

    def delete_reminder(self, text, date):
        # Удаление напоминания
        self.reminder_model.delete_reminder(text, date)

    def get_reminders(self, date):
        # Получение всех напоминаний на указанную дату
        reminders = self.reminder_model.get_reminders(date)
        return reminders

    def get_all_reminders(self):
        # Получение всех напоминаний
        reminders = self.reminder_model.get_all_reminders()
        return reminders

    def delete_all_reminders(self):
        # Удаление всех напоминаний
        self.reminder_model.delete_all_reminders()
        
            
