from TaskStatus import TaskStatus
from datetime import date

class Task:
    def __init__(self, name, deadline, description):
        self.__name = name
        self.__status = TaskStatus.TODO
        self.__deadline = deadline if isinstance(deadline, date) else None
        self.__priority = 5
        self.__description = description
        self.__category = ""

    def set_next_status(self):
        if(self.__status == TaskStatus.TODO):
            self.__status = TaskStatus.IN_PROGRESS
        elif(self.__status == TaskStatus.IN_PROGRESS):
            self.__status = TaskStatus.FINISHED
        else:
            print("Task is already finished")

    def set_new_priority(self, new_priority):
        if( new_priority < 0 or new_priority >10):
            print("Priority has to be between 0 and 10")
        else:
            self.__priority = new_priority

    def set_description(self, new_description):
        self.__description = new_description

