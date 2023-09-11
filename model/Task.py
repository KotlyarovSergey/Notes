import datetime


class Task:
    def __init__(self, title, body) -> None:
        self.__title__ = title
        self.__body__ = body
        self.__datetime__ = datetime.datetime.now()
        pass

    def get_title(self):
        return self.__title__
    
    def set_title(self, title):
        self.__title__ = title
        pass

    def get_body(self):
        return self.__body__
    
    def set_body(self, body):
        self.__body__ = body
        pass

    def get_datetime(self):
        return self.__datetime__
    
    def set_datetime(self):
        self.__datetime__ = datetime.datetime.now
        pass
