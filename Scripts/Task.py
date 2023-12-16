from TaskStatus import TaskStatus
from datetime import date


class Task:
    def __init__(self, name, status, deadline, priority, description):
        self.__name = name
        self.__status = status if isinstance(status, TaskStatus) else TaskStatus.TODO
        self.__deadline = deadline if isinstance(deadline, date) else "No deadline yet"
        self.__priority = priority if priority >= 0 and priority <= 10 else 5
        self.__description = description
        self.__personId = None

    def get_name(self):
        return self.__name

    def get_status(self):
        return self.__status

    def get_deadline(self):
        return self.__deadline

    def get_priority(self):
        return self.__priority

    def get_description(self):
        return self.__description

    def get_personId(self):
        return self.__personId
    def set_next_status(self):
        if (self.__status == TaskStatus.TODO):
            self.__status = TaskStatus.IN_PROGRESS
        elif (self.__status == TaskStatus.IN_PROGRESS):
            self.__status = TaskStatus.FINISHED
        else:
            print("Task is already finished")

    def set_new_priority(self, new_priority):
        if (new_priority < 0 or new_priority > 10):
            print("Priority has to be between 0 and 10")
        else:
            self.__priority = new_priority

    def set_description(self, new_description):
        self.__description = new_description

    def set_personId(self,id):
        self.__personId = id

if __name__ == '__main__':
    taak1 = Task("Taak1","","",5,"")
    print(taak1.get_status())
    taak1.set_next_status()
    print(taak1.get_status())
    taak1.set_next_status()
    print(taak1.get_status())
