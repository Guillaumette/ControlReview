from abc import ABC

import tabulate

from module.menu import Menu

class Delete(Menu, ABC):

    def execute(self, notes: dict) -> dict:
        key = int(input("Введите номер заметки: "))
        print(tabulate.tabulate([['id', 'название', 'описание', 'дата изменения'], notes[key].to_list()]))
        if input('Удалить? Д/Н').upper() == 'Д':
            notes.pop(key)
            print('Заметка удалена')
        else:
            print('Удаление отменено')
        return notes