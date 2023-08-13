from abc import ABC

import tabulate

from module.menu import Menu


class ShowId(Menu, ABC):

    def execute(self, notes: dict) -> dict:
        key = int(input("Введите номер заметки: "))
        print(tabulate.tabulate([['id', 'название', 'описание', 'дата изменения'], notes[key].to_list()]))
        return notes