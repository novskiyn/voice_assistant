from app.services.reminder_service import ReminderService
from datetime import datetime, timedelta
import re
import locale

# Установка русского языка для обработки дат
try:
    locale.setlocale(locale.LC_TIME, 'ru_RU.UTF-8')
except locale.Error:
    locale.setlocale(locale.LC_TIME, 'ru_RU')

class ReminderController:
    def __init__(self):
        self.reminder_service = ReminderService()

    def create_reminder(self, command):
        # Создание напоминания
        match = re.search(r"создай напоминание (.*?) на (.+)", command)
        if match:
            reminder_text = match.group(1).strip()
            date_text = match.group(2).strip()
            date = self.parse_date(date_text)
            if date:
                self.reminder_service.create_reminder(reminder_text, date)
                print(f"Напоминание '{reminder_text}' создано на {date}.")
            else:
                print("Укажите корректную дату напоминания.")
        else:
            print("Неправильный формат команды. Используйте: 'создай напоминание (напоминание) на (дата)'.")   

    def edit_reminder(self, command):
    # Редактирование напоминания
        match = re.search(r"отредактируй напоминание (.*) на (.*) в (.*)", command)
        if match:
            old_text = match.group(1).strip()
            old_date = match.group(2).strip()
            new_text = match.group(3).strip()
            old_date = self.parse_date(old_date)
            if old_date:
                self.reminder_service.edit_reminder(old_text, old_date, new_text)
                print(f"Напоминание '{old_text}' отредактировано в '{new_text}'.")
            else:
                print("Укажите корректную дату.")
        else:
            print("Неправильный формат команды. Используйте: 'отредактируй напоминание (старый текст) на (дата) в (новый текст)'.")

    def delete_reminder(self, command):
        # Удаление напоминания
        match = re.search(r"удали напоминание (.*) на (.*)", command)
        if match:
            reminder_text = match.group(1).strip()
            date_text = match.group(2).strip()
            date = self.parse_date(date_text)
            if date:
                self.reminder_service.delete_reminder(reminder_text, date)
                print(f"Напоминание '{reminder_text}' удалено.")
            else:
                print("Укажите корректную дату.")
        else:
            print("Неправильный формат команды. Используйте: 'удали напоминание (текст) на (дата)'.")

    def show_reminders(self, command):
        # Показ напоминаний на указанную дату
        match = re.search(r"покажи напоминание на (.+)", command)
        if match:
            date_text = match.group(1).strip()
            date = self.parse_date(date_text)
            if date:
                reminders = self.reminder_service.get_reminders(date)
                if reminders:
                    print(f"Напоминания на {date}:")
                    for reminder in reminders:
                        print(f"- {reminder[0]}")
                else:
                    print(f"На {date} нет напоминаний.")
            else:
                print("Укажите корректную дату.")
        else:
            print("Неправильный формат команды. Используйте: 'покажи напоминание на (дата)'.")

    def show_all_reminders(self):
        # Показ всех напоминаний
        reminders = self.reminder_service.get_all_reminders()
        if reminders:
            print("Все напоминания:")
            for reminder in reminders:
                print(f"- {reminder[0]} на {reminder[1]}")
        else:
            print("Нет напоминаний.")

    def delete_all_reminders(self):
        # Удаление всех напоминаний
        self.reminder_service.delete_all_reminders()
        print("Все напоминания удалены.")        

    def parse_date(self, input_text):
        # Парсинг даты из текста
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
            # Разделяем число и месяц из текста
            parts = input_text.split()
            if len(parts) != 2:
                raise ValueError("Некорректный формат даты. Ожидается: 'число месяц'.")

            day = int(parts[0])
            month_name = parts[1]

            # Проверяем, что месяц корректный
            if month_name not in months:
                raise ValueError(f"Некорректное название месяца: {month_name}")

            month = months[month_name]
            year = datetime.now().year

            # Создаем объект даты и возвращаем в нужном формате
            date = datetime(year=year, month=month, day=day)
            return date.strftime("%Y-%m-%d")

        except Exception as e:
            print(f"Ошибка: {str(e)}")
            return None
