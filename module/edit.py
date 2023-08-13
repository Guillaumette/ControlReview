from abc import ABC
import tabulate
from module.menu import Menu

class Edit(Menu, ABC):

    def execute(self, notes: dict) -> dict:
        key = int(input('Введите номер заметки: '))
        print(tabulate.tabulate([['id', 'название', 'описание', 'дата изменения'], notes[key].to_list()]))
        if input("Редактировать? Д/Н").upper() == 'Д':
            name = input('Введите новое название: ')
            body = input('Отредактируйте содержание: ')
            notes[key].__set__(name, body)
            print("Успешно отредактировано!")
        else:
            print("Редактирование отменено")
        return notes