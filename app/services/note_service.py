from app.models.note_model import NoteModel
from app.services.voice_service import VoiceService

class NoteService:
    def __init__(self):
        self.note_model = NoteModel()
        self.voice_service = VoiceService()

    def create_note(self, title):
        note = {"title": title, "type": "", "text": "", "points": []}
        print("Какой тип заметки вы хотите создать? С пунктами или без?")
        note_type = self.voice_service.recognize_speech().strip()

        if note_type == "с пунктами":
            note['type'] = "with_points"
            print("Произносите пункты заметки. Для завершения скажите 'сохранить'.")
            point_number = 1
            while True:
                print(f"Пункт {point_number}:")
                point = self.voice_service.recognize_speech().strip()
                if point.lower() == "сохранить":
                    break
                # Удаление ключевых слов из пункта
                for i in range(1, 21):  # Удаление ключевых слов для первых 20 пунктов
                    point = point.replace(f"пункт {self.get_ordinal(i)}", "").replace(f"{self.get_ordinal(i)} пункт", "").strip()
                if point:
                    note['points'].append(point)
                point_number += 1
        elif note_type == "без пунктов":
            note['type'] = "without_points"
            print("Произносите текст заметки.")
            note['text'] = self.voice_service.recognize_speech().strip()
        else:
            print("Неправильный тип заметки. Выберите 'с пунктами' или 'без пунктов'.")
            return

        self.note_model.save_note(note)
        print(f"Заметка '{title}' успешно сохранена.") 

    def edit_note(self, old_title, new_title):
        note = self.note_model.get_note(old_title)
        if note:
            note['title'] = new_title
            self.note_model.save_note(note)
            print(f"Заметка '{old_title}' успешно переименована в '{new_title}'.")
            return True
        print(f"Заметка '{old_title}' не найдена.")
        return False

    def delete_note(self, title):
        success = self.note_model.delete_note(title)
        if success:
            print(f"Заметка '{title}' успешно удалена.")
        else:
            print(f"Заметка '{title}' не найдена.")
        return success

    def delete_point(self, command):
        match = re.search(r"удали пункт (.*) из заметки (.*)", command)
        if match:
            point_text = match.group(1).strip()
            note_title = match.group(2).strip()
            # Преобразование порядкового числительного в номер
            point_index = self.get_point_index(point_text)
            if point_index is not None:
                self.note_service.delete_point(note_title, point_index)
            else:
                print("Неправильный формат пункта. Используйте порядковое числительное (первый, второй, третий и т.д.).")
        else:
            print("Неправильный формат команды. Используйте: 'удали пункт (номер) из заметки (название)'.")

    def get_ordinal(self, number):
        ordinals = {
            1: "первый",
            2: "второй",
            3: "третий",
            4: "четвёртый",
            5: "пятый",
            6: "шестой",
            7: "седьмой",
            8: "восьмой",
            9: "девятый",
            10: "десятый",
            11: "одиннадцатый",
            12: "двенадцатый",
            13: "тринадцатый",
            14: "четырнадцатый",
            15: "пятнадцатый",
            16: "шестнадцатый",
            17: "семнадцатый",
            18: "восемнадцатый",
            19: "девятнадцатый",
            20: "двадцатый"
        }
        return ordinals.get(number, str(number))           

    def get_note(self, title):
        note = self.note_model.get_note(title)
        if note:
            print(f"Заметка '{title}' найдена.")
        else:
            print(f"Заметка '{title}' не найдена.")
        return note

    def get_all_notes(self):
        notes = self.note_model.get_all_notes()
        if notes:
            print("Все заметки успешно загружены.")
        else:
            print("Нет заметок.")
        return notes
