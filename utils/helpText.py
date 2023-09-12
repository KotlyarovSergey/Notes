def getHelpText():
    text = "all - показать все записи\n"
    text += "select - выбрать записи\n"
    # text += "at dd.mm.yyyy - показать записи за один день dd.mm.yyyy\n"
    # text += "before dd.mm.yyyy - показать записи до dd.mm.yyyy\n"
    # text += "after dd.mm.yyyy - показать записи начиная с dd.mm.yyyy\n"
    # text += "between dd.mm.yyyy dd.mm.yyyy - показать записи между датами\n"
    text += "add - добавить запись\n"
    text += "del - удалить запись\n"
    text += "mod - изменить запись\n"
    text += "help - список комманд\n"
    text += "exit - выход"
    return text

def getShowParamsToSelect():
    text = "all - показать все записи\n"
    text += "day - показать записи за один день\n"
    text += "before - показать записи до указанной даты\n"
    text += "after - показать записи начиная с указанной даты\n"
    text += "between - показать записи между датами\n"
    return text