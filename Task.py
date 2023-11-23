from TaskStatus import TaskStatus

class Task:
    def __init__(self):
        self.__name = ""
        self.__status = TaskStatus.TODO
        self.__deadline = ""
        self.__priority = ""
        self.__description = ""
        self.__category = ""


