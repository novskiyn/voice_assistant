
class NoteController:
    def create_note(self, text):
        # Создание заметки
        note = {
            "text": text,
            "date": "2024-12-20"
        }
        # Сохранение заметки в базе данных
        print(f"Заметка создана: {note['text']}")
