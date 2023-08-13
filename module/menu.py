from abc import abstractmethod

class Menu:
    _name: str
    _description: str

    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description


    def get_name(self):
        return self.name

    def get_description(self):
        return self.description

    @abstractmethod
    def execute(self, notes: list) -> list:
        pass