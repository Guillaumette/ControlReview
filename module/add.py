from abc import ABC
from datetime import datetime

from data.note import Note
from module.menu import Menu

class Add(Menu, ABC):

    def execute(self, notes: dict) -> dict:
        name = input("Введите название заметки: ")
        body = input("Введите содержание: ")
        last_id = 0
        if notes:
            last_id = max(notes)
        note = Note(last_id + 1, name,body, datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        notes[note.get_id()] = note
        print("Заметка успешно добавлена!")
        return notes