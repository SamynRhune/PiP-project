from Task import Task
from TaskStatus import TaskStatus
from Person import Person
from DatabaseManager import DatabaseManager
from DateChecker import DateChecker


class CommandoHandler:
    def __init__(self):

        self.__firstLineCommands = ["ADD", "REMOVE", "UPDATE", "GET", "HELP", "EXPORT", "EXIT"]
        self.__add = ["TASK", "PERSON"]
        self.__remove = ["TASK", "PERSON"]
        self.__update = ["TASK"]
        self.__updateTask = ["STATUS", "DEADLINE", "PRIORITY", "PERSON"]
        self.__get = ["ALLTASK", "ALLPERSON","TASKWITHPERSON","PERSONTASKCOUNT","TASKTODO","TASKINPROGRESS","TASKFINISHED","TASKNOTFINISHED","TASKFROMALLPEOPLE","TASKFROMPERSON"]
        self.__dbManager = DatabaseManager()

    def inputCommand(self, command):
        splitted_command = command.split(" ")

        if len(splitted_command) == 1 or len(splitted_command) == 2:
            self.eenCommand(splitted_command)
        else:
            print("Ongeldig commando typ HELP om alle mogelijke commando's te bekijken")

    def eenCommand(self, commandlist):

        # ADD
        if commandlist[0] == self.__firstLineCommands[0]:
            if len(commandlist) == 1:
                options = ""
                for item in self.__add:
                    options += item + " of "
                options = options[:-3]
                commandlist.append(input("Wat wil je toevoegen " + options + "\n").upper())
            self.addCommand(commandlist)

        # REMOVE
        elif commandlist[0] == self.__firstLineCommands[1]:
            if len(commandlist) == 1:
                options = ""
                for item in self.__remove:
                    options += item + " of "
                options = options[:-3]
                commandlist.append(input("Wat wil je verwijderen " + options + "\n").upper())
            self.removeCommand(commandlist)

        # UPDATE
        elif commandlist[0] == self.__firstLineCommands[2]:
            if len(commandlist) == 1:
                options = ""
                for item in self.__update:
                    options += item + " of "
                options = options[:-3]
                commandlist.append(input("Wat wil je updaten " + options + "\n").upper())
            self.updateCommand(commandlist)

        # GET
        elif commandlist[0] == self.__firstLineCommands[3]:
            if len(commandlist) == 1:
                options = ""
                for item in self.__get:
                    options += item + " of "
                options = options[:-3]
                commandlist.append(input("Wat wil je bekijken \n" + options + "\n").upper())
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
        elif commandlist[0] == self.__firstLineCommands[6]:
            # Laten doorgaan voor main want deze is exit
            self.__dbManager.closeConnectionDb()
        else:
            print("Je hebt een verkeerd commando ingegeven typ help om alle commando's te krijgen.")

    def addCommand(self, commandlist):
        # TAAK
        if commandlist[1] == self.__add[0]:
            print("\n------------------\nTOEVOEGEN VAN TAAK\n------------------")
            name = input("Geef de naam van de taak:\n")
            description = input("Geef beschrijving van de taak:\n")

            taak = Task(name, TaskStatus.TODO, "No deadline", 5, description)
            self.__dbManager.addTask(taak)

            print("Toevoegen taak gelukt\n")

        # PERSON
        elif commandlist[1] == self.__add[1]:
            print("\n------------------\nTOEVOEGEN VAN PERSOON\n------------------")
            name = input("Geef de naam van de persoon:\n")

            birthday = DateChecker("")
            while not birthday.checkValid():
                bday = input("Geef geboortedag van de persoon (DD-MM-YYYY):\n")
                birthday = DateChecker(bday)

            person = Person(name, birthday.getDate())
            self.__dbManager.addPerson(person)

            print("Toevoegen persoon gelukt\n")
        else:
            self.backToMainWrongSecondArgument()

    def removeCommand(self, commandlist):
        # TASK
        if commandlist[1] == self.__remove[0]:
            print("\nTaak verwijderen ...\n")
            id = self.getIdFromTaskToUpdate()
            self.__dbManager.removeTask(id)

        # PERSON
        elif commandlist[1] == self.__remove[1]:
            print("\nPersoon verwijderen ...\n")
            id = self.getIdFromPersonToUpdate()
            self.__dbManager.removePerson(id)
        else:
            self.backToMainWrongSecondArgument()

    def updateCommand(self, commandlist):
        # TASK
        if commandlist[1] == self.__update[0]:
            if len(commandlist) == 2:
                options = ""
                for item in self.__updateTask:
                    options += item + " of "
                options = options[:-3]
                commandlist.append(input("Wat wil je updaten " + options +  "\n").upper())
            self.updateTaskCommand(commandlist);
        else:
            self.backToMainWrongSecondArgument()

    def getIdFromTaskToUpdate(self):
        self.__dbManager.getAllTasks()
        print("\n------------------\nAANPASSEN VAN TASK\n------------------")
        id = input("Geef het id van de taak die je wil aanpassen:\n")
        return id

    def getIdFromPersonToUpdate(self):
        print("\n------------------\nALLE PERSONEN\n------------------")
        self.__dbManager.getAllPeople()
        print("\n------------------\nAANPASSEN VAN PERSOON\n------------------")
        id = input("Geef het id van de persoon die je wil aanpassen:\n")
        return id

    def updateTaskCommand(self, commandlist):

        # Status
        print("\nStatus updaten ...\n")
        if commandlist[2] == self.__updateTask[0]:
            id = self.getIdFromTaskToUpdate()
            self.__dbManager.setNextStatusTask(id);

        # Deadline
        elif commandlist[2] == self.__updateTask[1]:
            print("\nDeadline updaten ...\n")
            id = self.getIdFromTaskToUpdate()
            deadline = DateChecker("")
            while not deadline.checkValid():
                date = input("Geef een Deadline in de vorm DD-MM-YYYY\n")
                deadline = DateChecker(date)

            self.__dbManager.updateTaskDeadline(id, deadline.getDate())

        # Priority
        elif commandlist[2] == self.__updateTask[2]:
            print("\nPriority updaten ...\n")
            id = self.getIdFromTaskToUpdate()
            deadline = input("Geef een prioriteit van 0 tot 10\n")
            self.__dbManager.updateTaskPriority(id, deadline)

        #Person
        elif commandlist[2] == self.__updateTask[3]:
            print("\nPersoon toewijzen ...\n")
            taskId = self.getIdFromTaskToUpdate()
            personId = self.getIdFromPersonToUpdate()

            self.__dbManager.updateTaskPerson(taskId, personId)
        else:
            self.backToMainWrongSecondArgument()



    def getCommand(self, commandlist):
        # ALLTASK
        if commandlist[1] == self.__get[0]:
            self.__dbManager.getAllTasks()
            print("\n")

        # ALLPERSON
        elif commandlist[1] == self.__get[1]:
            self.__dbManager.getAllPeople()
            print("\n")

        #TASKWITHPERSON
        elif commandlist[1] == self.__get[2]:
            self.__dbManager.getAllTasksWithPerson()
            print("\n")
        #PERSONWITHCOUNTTASK
        elif commandlist[1] == self.__get[3]:
            self.__dbManager.getAllPeopleWithCountTask()
            print("\n")
        #TASKSTODO
        elif commandlist[1] == self.__get[4]:
            self.__dbManager.getAllTasksTodo()
            print("\n")
        #TASKSINPROGRESS
        elif commandlist[1] == self.__get[5]:
            self.__dbManager.getAllTasksProgress()
            print("\n")
        #TASKSFINISHED
        elif commandlist[1] == self.__get[6]:
            self.__dbManager.getAllTasksFinished()
            print("\n")
        #TASKSNOTFINISHED
        elif commandlist[1] == self.__get[7]:
            self.__dbManager.getAllTasksNotFinished()
            print("\n")

        # TASKSFROMALLPEOPLE
        elif commandlist[1] == self.__get[8]:
            self.__dbManager.getAllTasksFromAllPeople()
            print("\n")
        # TASKSFROMPERSON
        elif commandlist[1] == self.__get[9]:
            self.__dbManager.getAllPeople();
            print("\n")
            id = -1
            while(not self.__dbManager.doesTaskExist(id)):
                id = input("Geef het ID van de persoon waarvan je de taken wilt zien:\n");


            self.__dbManager.getAllTasksFromPerson(id)
            print("\n")
        else:
            self.backToMainWrongSecondArgument()

    def backToMainWrongSecondArgument(self):
        # terug naar het hoofdmenu gaat automatisch

        print("\nVerkeerde Tweede Argument\nBack To Main ... \n")