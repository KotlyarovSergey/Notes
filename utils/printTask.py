from model.Task import Task

def taskToSting(task: Task):
    result = f"\tЗаголовок: {task.get_title()}\n"
    result += f"\tОписание: {task.get_body()}\n"
    dt = task.get_datetime()
    result += f"\tДата: {dt.year}-{dt.month}-{dt.day} {dt.hour:02d}:{dt.minute:02d}:{dt.second:02d}"
    
    return result