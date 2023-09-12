from model.Task import Task
import utils.helpText

class Viewer:
    def showMessage(self, message):
        print(message)

    def showTasks(self, tasks: list[Task]):
        index = 0
        for task in tasks:
            print(f"Номер: {index}")
            print(utils.printTask.taskToSting(task))
            index += 1
