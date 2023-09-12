from model.Task import Task
import utils.jsonParser
import utils.printTask
from io import open
import json


class Repository:
    def __init__(self, dataFileName) -> None:
        self.__file__ = dataFileName
        self.__tasks__ = self.__loadTasksFromFile()
        print("Загружено: ", len(self.__tasks__), " записей")
        pass


    def addTask(self, task):
        self.__tasks__.append(task)
        self.__saveTasksToFile()
        return

    def getTasks(self, condition) -> list[Task]:
        selectedTasks:list[Task] = []
        for task in self.__tasks__:
            if (condition(task)):
                selectedTasks.append(task)
        return selectedTasks

    def removeAtIndex(self, index):
        try:
            self.__tasks__.pop(index)
            self.__saveTasksToFile()
        except:
            print("Неверный индекс!")
    
    def removeTask(self, task: Task):
        try:
            self.__tasks__.remove(task)
            self.__saveTasksToFile()
        except:
            print(f"Задача \"{task.get_title}\" не надена!")

    def updateTaskAtIndex(self, index, newTask):
        if(index < 0 or index >= len(self.__tasks__)):
            print("Неверный индекс!")
        else:
            self.__tasks__[index] = newTask
            self.__saveTasksToFile()

    def updateTask(self, oldTask, newTask):
        try:
            index = self.__tasks__.index(oldTask)
            self.__tasks__[index] = newTask
        except:
            print(f"Задача \"{oldTask.get_title}\" не надена!")


    def __saveTasksToFile(self):
        with open(self.__file__, "w") as write_file:
            json.dump(self.__tasks__, write_file, default=utils.jsonParser.toJson)

    def __loadTasksFromFile(self) -> list[Task]:
        with open(self.__file__, "r") as read_file:
            lst = json.load(read_file)
            return utils.jsonParser.toTask(lst)
            