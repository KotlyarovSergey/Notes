from model.Task import Task
import datetime


def toJson(obj):
    if isinstance(obj, Task):
        dt: datetime.datetime = obj.get_datetime()
        dtTuple = (dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second)
        return (obj.get_title(), obj.get_body(), dtTuple)
    
def toTask(listOfTasks):
    result = []
    for task in listOfTasks:
        (title, body, dt) = task
        (yr, mon, day, hour, min, sec) = dt
        result.append(Task(title, body, datetime.datetime(yr, mon, day, hour, min, sec)))
    return result
        

    

