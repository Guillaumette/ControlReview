from datetime import datetime

class Note:
    id: int
    _name: str
    _body: str
    _date: str

    def __init__(self, id: int, name: str, body: str, date: str) -> None:
        self.id = id
        self.name = name
        self.body = body
        self.date = date

    def __set__(self, name: str,body: str) -> None:
        self.name = name
        self.body = body
        self.date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def get_id(self) -> int:
        return self.id

    def get_date(self) -> str:
        return self.date

    def to_list(self) -> list:
        return [self.id, self.name, self.body, self.date]