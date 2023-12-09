from Task import Task
from TaskStatus import TaskStatus
from DatabaseManager import DatabaseManager


class CommandoHandler:
    def __init__(self):

        self.__firstLineCommands = ["ADD", "REMOVE", "HELP"]
        self.__add = ["TASK", "PERSON"]
        self.__dbManager = DatabaseManager()

    def inputCommand(self, command):
        splitted_command = command.split(" ")

        if len(splitted_command) == 1 or len(splitted_command) == 2:
            self.eenCommand(splitted_command)
        else:
            print("Ongeldig commando typ help om alle mogelijke commando's te bekijken")

    def eenCommand(self, commandlist):
        if commandlist[0].upper() == self.__firstLineCommands[0]:
            if commandlist[1] is None:
                commandlist[1] = input("Wat wil je toevoegen TASK of PERSON")
            self.addCommand(commandlist)
        else:
            # NOG TOEVOEGEN
            print("Nog toevoegen")

    def addCommand(self, commandlist):
        if commandlist[1] == self.__add[0]:
            print("TOEVOEGEN VAN TAAK")
            print("------------------")
            name = input("Geef de naam van de taak: ")
            description = input("Geef beschrijving van de taak: ")

            taak = Task(name, TaskStatus.TODO, "No deadline", 5, description)
            self.__dbManager.addTask(taak)
