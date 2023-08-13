import json
from abc import ABC

from module.menu import Menu

class Save(Menu, ABC):

    def execute(self, notes: dict) -> dict:
        if notes:
            with open(f"{input('Введите название файла: ')}.json", "w", encoding="UTF-8") as file:
                file.write(json.dumps(notes, default=lambda x: x.__dict__, ensure_ascii=False))
        else:
            print("База пуста")
        print("Сохранение успешно!")
        return notes