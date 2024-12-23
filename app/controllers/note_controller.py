import re
from app.services.note_service import NoteService

class NoteController:
    def __init__(self):
        self.note_service = NoteService()

    def create_note(self, command):
        match = re.search(r"создай заметку (.*)", command)
        if match:
            note_title = match.group(1).strip()
            self.note_service.create_note(note_title)
        else:
            print("Неправильный формат команды. Используйте: 'сохрани заметку (название)'.")

    def edit_note(self, command):
        match = re.search(r"отредактируй заметку (.*) в (.*)", command)
        if match:
            old_title = match.group(1).strip()
            new_title = match.group(2).strip()
            self.note_service.edit_note(old_title, new_title)
        else:
            print("Неправильный формат команды. Используйте: 'отредактируй заметку (старое название) в (новое название)'.")

    def delete_note(self, command):
        match = re.search(r"удали заметку (.*)", command)
        if match:
            note_title = match.group(1).strip()
            self.note_service.delete_note(note_title)
        else:
            print("Неправильный формат команды. Используйте: 'удали заметку (название)'.")

    def delete_point(self, command):
        match = re.search(r"удали пункт (\d+) из заметки (.*)", command)
        if match:
            point_index = int(match.group(1).strip()) - 1  # Номера начинаются с 1
            note_title = match.group(2).strip()
            self.note_service.delete_point(note_title, point_index)
        else:
            print("Неправильный формат команды. Используйте: 'удали пункт (номер) из заметки (название)'.")

    def show_notes(self, command):
        match = re.search(r"покажи заметку (.*)", command)
        if match:
            note_title = match.group(1).strip()
            note = self.note_service.get_note(note_title)
            if note:
                print(f"Заметка '{note_title}':")
                if note['type'] == 'with_points':
                    for i, point in enumerate(note['points'], 1):
                        print(f"{i}. {point}")
                else:
                    print(note['text'])
        else:
            print("Неправильный формат команды. Используйте: 'покажи заметку (название)'.")

    def show_all_notes(self):
        notes = self.note_service.get_all_notes()
        if notes:
            print("Все заметки:")
            for note_title in notes:
                print(f"- {note_title}")
