from control.control import Control
from module.add import Add
from module.delete import Delete
from module.edit import Edit
from module.exit import Exit
from module.read import Read
from module.save import Save
from module.show_all import ShowAll
from module.show_date import ShowDate
from module.show_id import ShowId


def start(control):
    print('======МЕНЮ======\n', 'help - все команды\n')
    while True:
        try:
            key = input(': ')
            control.on_execute(key)
        except KeyboardInterrupt:
            print("Выход")
            exit()


class View:
    control: Control

    def __init__(self):
        notes = {}
        self.control = Control(notes, [Read('read', 'считывать из файла'),
                                       Edit('edit', 'редактировать'),
                                       Add('add', 'добавить'),
                                       Delete('del', 'удалить'),
                                       Save('save', 'сохранить в файл'),
                                       ShowAll('showall', 'просмотреть всю базу'),
                                       ShowId('showid', 'посмотреть по номеру'),
                                       ShowDate('showdate', 'посмотреть по дате'),
                                       Exit('exit', 'выход')])
        start(self.control)

    def get_control(self) -> Control:
        return self.control