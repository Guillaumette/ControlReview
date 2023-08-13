import tabulate

class Control:
    _menu: dict
    _notes: dict

    def __init__(self, notes: dict, menu: list):
        self.notes = notes
        tmp = {}
        for m in menu:
            tmp[m.get_name()] = m
        self.menu = tmp

    def get_notes(self):
        return self.notes

    def get_menu(self):
        return self.menu

    def on_execute(self, key: str):
        if key == 'help':
            self.help()
        else:
            try:
                self.notes = self.menu[key].execute(self.notes)
            except KeyError:
                print("Значение неверно")

    def help(self):
        tmp = []
        for k, v in self.get_menu().items():
            tmp.append([k, v.get_description()])
        print(tabulate.tabulate(tmp))