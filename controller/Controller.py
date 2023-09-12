from model.Repository import Repository
from model.Task import Task
from viewer.Viewer import Viewer
import utils.helpText
import datetime



class Contlroller:
    def __init__(self, repo: Repository, view: Viewer) -> None:
        self.__repo__ = repo
        self.__view__ = view
        self.__selectTasks__: list[Task]
        self.__selectAllTasks__()
        pass
    
    
    def run(self):
        helpText = utils.helpText.getHelpText()
        self.__view__.showMessage(helpText)
        while(True):
            userInput = input("\nВведите команду: ").strip().lower()
            match userInput:
                case "exit":
                    break
                case "help":
                    self.__view__.showMessage(helpText)
                case "all":
                    self.__selectAllTasks__()
                    self.__showTasks__(self.__selectedTasks__)
                case "add":
                    self.__addTask__()
                case "select":
                    self.__selectTasks__()
                case "del":
                    self.__deleteTask__()
                case "mod":
                    self.__modifiedTask__()
                case _:
                    self.__view__.showMessage("Ошибка. Команда не распознана.")

    

    def __addTask__(self):
        self.__view__.showMessage("\n\tДобавление новой заметки")
        task = self.__inputTask__()
        self.__repo__.addTask(task)
    
    def __inputTask__(self) -> Task:
        head = input("Введите заголовок: ")
        body = input("Введите содержание заметки: ")
        return Task(head, body, datetime.datetime.now())

    def __selectTasks__(self):
        self.__view__.showMessage(utils.helpText.getShowParamsToSelect())
        self.__view__.showMessage("Введите данные для фильтрации: ")
        userInput = input("Введите команду: ").strip().lower()
        match userInput:
            case "all":
                self.__selectAllTasks__()
                self.__showTasks__(self.__selectedTasks__)
            case "day":
                day = self.__inputDate__("Введите день в формате dd.mm.yyyy: ")
                if day != None:
                    after = datetime.datetime(day.year, day.month, day.day, 0, 0, 0)
                    before = after + datetime.timedelta(days=1)
                    self.__selectedTasks__ = self.__repo__.getTasks(lambda x: (x.get_datetime() >= after and x.get_datetime() < before))
                    self.__showTasks__(self.__selectedTasks__)
                else:
                    self.__view__.showMessage("Ошибка. Команда не распознана.")
            case "after":
                after = self.__inputDate__("День начала отбора (dd.mm.yyyy): ")
                if after != None:
                    self.__selectedTasks__ = self.__repo__.getTasks(lambda x: (x.get_datetime() >= after))
                    self.__showTasks__(self.__selectedTasks__)
                else:
                    self.__view__.showMessage("Ошибка. Команда не распознана.")
            case "before":
                before = self.__inputDate__("Отобрать до дня (dd.mm.yyyy): ")
                if before != None:
                    self.__selectedTasks__ = self.__repo__.getTasks(lambda x: (x.get_datetime() < before))
                    self.__showTasks__(self.__selectedTasks__)
                else:
                    self.__view__.showMessage("Ошибка. Команда не распознана.")
            case "between":
                after = self.__inputDate__("День начала отбора (dd.mm.yyyy): ")
                if after != None:
                    before = self.__inputDate__("Отобрать до дня (dd.mm.yyyy): ")
                    if before != None:
                        self.__selectedTasks__ = self.__repo__.getTasks(lambda x: (x.get_datetime() >= after and x.get_datetime() < before))
                        self.__showTasks__(self.__selectedTasks__)
                    else:
                        self.__view__.showMessage("Ошибка. Команда не распознана.")
                else:
                    self.__view__.showMessage("Ошибка. Команда не распознана.")
            case _:
                self.__view__.showMessage("Ошибка. Команда не распознана.")
    
    
    def __inputDate__(self, message) -> datetime.datetime:
        userInput = input(message).strip()
        lst = list(userInput.split('.'))
        if len(lst) != 3:
            return None
        
        try:
            day = int(lst[0])
            month = int(lst[1])
            year = int(lst[2])
            return datetime.datetime(year, month, day)
        except:
            return None


    def __selectAllTasks__(self):
        self.__selectedTasks__ = self.__repo__.getTasks(lambda x: True)

    def __showTasks__(self, tasks):
        self.__view__.showTasks(tasks)

    def __deleteTask__(self):
        self.__view__.showMessage("\n\tУдаление заметки")
        userInput = input("Введите номер удаляемой записи: ").strip()
        try:
            index = int(userInput)
            if index > 0 and index < len(self.__selectedTasks__):
                self.__repo__.removeTask(self.__selectedTasks__[index])
                self.__view__.showMessage("Удалено")
            else:
                self.__view__.showMessage("Ошибка. Неверный номер")    
        except:
            self.__view__.showMessage("Ошибка. Нужно число.")

    def __modifiedTask__(self):
        self.__view__.showMessage("\n\tИзменение заметки")
        userInput = input("Введите номер изменяемой записи: ").strip()
        try:
            index = int(userInput)
            if index > 0 and index < len(self.__selectedTasks__):
                newTask = self.__inputTask__()
                self.__repo__.updateTask(self.__selectedTasks__[index], newTask)
                self.__view__.showMessage("Успешно")
            else:
                self.__view__.showMessage("Ошибка. Неверный номер")    
        except:
            self.__view__.showMessage("Ошибка. Нужно число.")


