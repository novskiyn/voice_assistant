import sqlite3

class NoteModel:
    def __init__(self):
        try:
            self.conn = sqlite3.connect('notes.db')
            self.cursor = self.conn.cursor()
            self.cursor.execute('''CREATE TABLE IF NOT EXISTS notes
                                 (title TEXT PRIMARY KEY, type TEXT, text TEXT, points TEXT)''')
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Ошибка подключения к базе данных: {e}")

    def save_note(self, note):
        try:
            if note['type'] == 'with_points':
                points_str = ', '.join(note['points'])
                self.cursor.execute("INSERT OR REPLACE INTO notes VALUES (?, ?, ?, ?)",
                                    (note['title'], note['type'], '', points_str))
            else:
                self.cursor.execute("INSERT OR REPLACE INTO notes VALUES (?, ?, ?, ?)",
                                    (note['title'], note['type'], note['text'], ''))
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Ошибка сохранения заметки: {e}")

    def get_note(self, title):
        try:
            self.cursor.execute("SELECT * FROM notes WHERE title = ?", (title,))
            note = self.cursor.fetchone()
            if note:
                return {
                    "title": note[0],
                    "type": note[1],
                    "text": note[2],
                    "points": note[3].split(', ') if note[3] else []
                }
            return None
        except sqlite3.Error as e:
            print(f"Ошибка получения заметки: {e}")
            return None

    def get_all_notes(self):
        try:
            self.cursor.execute("SELECT title FROM notes")
            notes = self.cursor.fetchall()
            return [note[0] for note in notes]
        except sqlite3.Error as e:
            print(f"Ошибка получения всех заметок: {e}")
            return []

    def delete_note(self, title):
        try:
            self.cursor.execute("DELETE FROM notes WHERE title = ?", (title,))
            self.conn.commit()
            return self.cursor.rowcount > 0
        except sqlite3.Error as e:
            print(f"Ошибка удаления заметки: {e}")
            return False
