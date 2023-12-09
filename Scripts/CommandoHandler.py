from Task import Task
from TaskStatus import TaskStatus
from Person import Person
from DatabaseManager import DatabaseManager


class CommandoHandler:
    def __init__(self):

        self.__firstLineCommands = ["ADD", "REMOVE", "UPDATE", "GET", "HELP", "EXPORT", "EXIT"]
        self.__add = ["TASK", "PERSON"]
        self.__remove = ["TASK", "PERSON"]
        self.__update = ["TASK"]
        self.__updateTask = ["STATUS", "DEADLINE", "PRIORITY"]
        self.__get = ["TASK", "PERSON"]
        self.__dbManager = DatabaseManager()

    def inputCommand(self, command):
        splitted_command = command.split(" ")

        if len(splitted_command) == 1 or len(splitted_command) == 2:
            self.eenCommand(splitted_command)
        else:
            print("Ongeldig commando typ HELP om alle mogelijke commando's te bekijken")

    def eenCommand(self, commandlist):
        # TODO string automatisch laten genereren
        # ADD
        if commandlist[0] == self.__firstLineCommands[0]:
            if len(commandlist) == 1:
                commandlist.append(input("Wat wil je toevoegen TASK of PERSON\n").upper())
            self.addCommand(commandlist)

        # REMOVE
        elif commandlist[0] == self.__firstLineCommands[1]:
            if len(commandlist) == 1:
                commandlist.append(input("Wat wil je verwijderen TASK of PERSON\n").upper())
            self.removeCommand(commandlist)

        # UPDATE
        elif commandlist[0] == self.__firstLineCommands[2]:
            if len(commandlist) == 1:
                commandlist.append(input("Wat wil je updaten TASK\n").upper())
            self.updateCommand(commandlist)

        # GET
        elif commandlist[0] == self.__firstLineCommands[3]:
            if len(commandlist) == 1:
                commandlist.append(input("Wat wil je bekijken TASK of PERSON\n").upper())
            self.getCommand(commandlist)

        # HELP
        elif commandlist[0] == self.__firstLineCommands[4]:
            print("\n------------------\nALLE COMMANDO'S\n------------------")
            for i in self.__firstLineCommands:
                print(i)

        elif commandlist[0] == self.__firstLineCommands[5]:
            print("\n------------------\nEXPORTEREN NAAR EXCEL\n------------------")
            self.__dbManager.exportToExcel()

        # EXIT
        else:
            # Laten doorgaan voor main want deze is exit
            print("Nog toevoegen")

    def addCommand(self, commandlist):
        # TAAK
        if commandlist[1] == self.__add[0]:
            print("\n------------------\nTOEVOEGEN VAN TAAK\n------------------")
            name = input("Geef de naam van de taak:\n ")
            description = input("Geef beschrijving van de taak:\n")

            taak = Task(name, TaskStatus.TODO, "No deadline", 5, description)
            self.__dbManager.addTask(taak)

            print("Toevoegen taak gelukt\n")

        # PERSON
        elif commandlist[1] == self.__add[1]:
            print("\n------------------\nTOEVOEGEN VAN PERSOON\n------------------")
            name = input("Geef de naam van de persson:\n")
            birthday = input("Geef geboortedag van de taak (DD-MM-YYYY):\n")

            person = Person(name, birthday)
            self.__dbManager.addPerson(person)

            print("Toevoegen persoon gelukt\n")
        else:
            # terug naar het hoofdmenu gaat automatisch
            print("Back To Main \n")

    def removeCommand(self, commandlist):
        # TASK
        if commandlist[1] == self.__remove[0]:
            print("\n------------------\nALLE TAKEN\n------------------")
            self.__dbManager.getAllTasks()
            print("\n------------------\nVERWIJDEREN VAN TASK\n------------------")
            id = input("Geef het id van de taak die je wil verwijderen:\n")
            self.__dbManager.removeTask(id)

        # PERSON
        elif commandlist[1] == self.__remove[1]:
            print("\n------------------\nALLE PERSONEN\n------------------")
            self.__dbManager.getAllPeople()
            print("\n------------------\nVERWIJDEREN VAN PERSOON\n------------------")
            id = input("Geef het id van de persoon die je wil verwijderen:\n")
            self.__dbManager.removePerson(id)

    def updateCommand(self, commandlist):
        # TASK
        if commandlist[1] == self.__update[0]:
            if len(commandlist) == 2:
                commandlist.append(input("Wat wil je updaten STATUS of DEADLINE of PRIORITY\n").upper())
            self.updateTaskCommand(commandlist);
        else:
            print("")
            # Ruimte voor uitbreidbaarheid

    def updateTaskCommand(self, commandlist):
        # TODO Alles in een dezelfde command zetten teveel herhaling
        # Status
        if commandlist[2] == self.__updateTask[0]:
            print("\n------------------\nALLE TAKEN\n------------------")
            self.__dbManager.getAllTasks()
            print("\n------------------\nUPDATEN VAN TASK\n------------------")
            id = input("Geef het id van de taak die je wil updaten:\n")
            self.__dbManager.setNextStatusTask(id);

        # Deadline
        elif commandlist[2] == self.__updateTask[1]:
            print("\n------------------\nALLE TAKEN\n------------------")
            self.__dbManager.getAllTasks()
            print("\n------------------\nUPDATEN VAN TASK\n------------------")
            id = input("Geef het id van de taak die je wil updaten:\n")
            deadline = input("Geef een Deadline in de vorm DD-MM-YYYY\n")

            self.__dbManager.updateTaskDeadline(id, deadline)

        # Priority
        elif commandlist[2] == self.__updateTask[2]:
            print("\n------------------\nALLE TAKEN\n------------------")
            self.__dbManager.getAllTasks()
            print("\n------------------\nUPDATEN VAN TASK\n------------------")
            id = input("Geef het id van de taak die je wil updaten:\n")
            deadline = input("Geef een prioriteit van 0 tot 10\n")
            self.__dbManager.updateTaskPriority(id, deadline)

    def getCommand(self, commandlist):
        # TASK
        if commandlist[1] == self.__get[0]:
            self.__dbManager.getAllTasks()
            print("\n")

        # PERSON
        elif commandlist[1] == self.__get[1]:
            self.__dbManager.getAllPeople()
            print("\n")
