# app/models/reminder_model.py
import sqlite3

class ReminderModel:
    def __init__(self):
        self.conn = sqlite3.connect('reminders.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS reminders
                             (text text, date text)''')
        self.conn.commit()

    def save_reminder(self, reminder):
        # Сохранение напоминания в базе данных
        self.cursor.execute("INSERT INTO reminders VALUES (?, ?)",
                            (reminder['text'], reminder['date']))
        self.conn.commit()

    def edit_reminder(self, old_text, old_date, new_text):
        # Редактирование напоминания в базе данных
        self.cursor.execute("UPDATE reminders SET text = ? WHERE text = ? AND date = ?",
                            (new_text, old_text, old_date))
        self.conn.commit()

    def delete_reminder(self, text, date):
        # Удаление напоминания из базы данных
        self.cursor.execute("DELETE FROM reminders WHERE text = ? AND date = ?",
                            (text, date))
        self.conn.commit()

    def get_reminders(self, date):
        # Получение всех напоминаний на указанную дату
        self.cursor.execute("SELECT * FROM reminders WHERE date = ?", (date,))
        reminders = self.cursor.fetchall()
        return reminders

    def get_all_reminders(self):
        # Получение всех напоминаний
        self.cursor.execute("SELECT * FROM reminders")
        reminders = self.cursor.fetchall()
        return reminders

    def delete_all_reminders(self):
        # Удаление всех напоминаний из базы данных
        self.cursor.execute("DELETE FROM reminders")
        self.conn.commit()    
