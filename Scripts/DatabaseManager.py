import sqlite3
from Task import Task
from TaskStatus import TaskStatus
from Person import Person
import pandas as pd
import os


class DatabaseManager:
    def __init__(self):

        current_directory = os.path.dirname(os.path.abspath(__file__))
        database_directory = os.path.join(current_directory,"..","Databases")

        #Databasedirectory aanmaken
        if not os.path.exists(database_directory):
            os.makedirs(database_directory)

        #connectie opzetten
        database_path = os.path.join(database_directory,"TaskDatabase.db")
        self.__connection = sqlite3.connect(database_path)
        self.__cursor = self.__connection.cursor()

        #controleren of tabellen al bestaan
        self.__cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='Person'")
        person_exists = self.__cursor.fetchone()
        if not person_exists:
            self.__cursor.execute('''CREATE TABLE "Person" (
	            "Id"	INTEGER,
	            "Name"	TEXT UNIQUE,
	            "Birthday"	TEXT,
	            PRIMARY KEY("Id")
                )''')
            self.__connection.commit()

        self.__cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='Task'")
        task_exists = self.__cursor.fetchone()
        if not task_exists:
            self.__cursor.execute('''CREATE TABLE "Task" (
                "Id"	INTEGER NOT NULL,
                "Name"	INTEGER NOT NULL UNIQUE,
                "Status"	TEXT NOT NULL,
                "Deadline"	INTEGER,
                "Priority"	INTEGER NOT NULL,
                "Description"	TEXT,
                "PersonId"	INTEGER,
                PRIMARY KEY("Id")
            )''')
            self.__connection.commit()

    def getAllTasks(self):
        myQuery = "SELECT Id,Name,Status,Deadline,Priority,Description,PersonId FROM Task"
        self.__cursor.execute(myQuery)

        rijen = self.__cursor.fetchall()

        print("---------------------")
        print("ALLE TAKEN")
        print("---------------------")

        df = pd.DataFrame(rijen, columns=['ID', 'Name', 'Status', 'Deadline', 'Priority', 'Description', 'PersonId'])

        df = df.fillna('None')
        pd.set_option('display.max_columns', None)
        pd.set_option('display.max_rows', None)
        print(df.to_string(index=False))



    def getAllPeople(self):
        myQuery = "SELECT Id,Name,Birthday FROM Person"
        self.__cursor.execute(myQuery)

        rijen = self.__cursor.fetchall()
        print("---------------------")
        print("ALLE PERSONEN")
        print("---------------------")

        df = pd.DataFrame(rijen, columns=["Id","Name","Birthday"])

        df = df.fillna('None')
        pd.set_option('display.max_columns', None)
        pd.set_option('display.max_rows', None)
        print(df.to_string(index=False))

    def getAllTasksWithPerson(self):

        myQuery = "SELECT Task.Id, Task.Name, Task.Status, Task.Deadline, Task.Priority, Task.Description, Person.Name, Person.Birthday FROM Task LEFT JOIN Person ON Task.PersonId = Person.Id;"

        self.__cursor.execute(myQuery)

        rijen = self.__cursor.fetchall()

        print("---------------------")
        print("ALLE TAKEN")
        print("---------------------")

        df = pd.DataFrame(rijen,
        columns=['ID', 'Name', 'Status', 'Deadline', 'Priority', 'Description', 'PersonName','PersonBirthday'])

        df = df.fillna('None')
        pd.set_option('display.max_columns', None)
        pd.set_option('display.max_rows', None)
        print(df.to_string(index=False))

    def getAllPeopleWithCountTask(self):
        myQuery = "SELECT Person.Id AS Id, Person.Name AS Name,Person.Birthday AS Birthday, COUNT(Task.Id) AS TaskCount FROM Person LEFT JOIN Task ON Person.Id = Task.PersonId GROUP BY Person.Id, Person.Name;"
        self.__cursor.execute(myQuery)

        rijen = self.__cursor.fetchall()
        print("---------------------")
        print("ALLE PERSONEN")
        print("---------------------")

        df = pd.DataFrame(rijen, columns=["Id","Name","Birthday","TaskCount"])

        df = df.fillna('None')
        pd.set_option('display.max_columns', None)
        pd.set_option('display.max_rows', None)
        print(df.to_string(index=False))

    def getAllTasksTodo(self):

        myQuery = "SELECT Task.Id, Task.Name, Task.Status, Task.Deadline, Task.Priority, Task.Description, PersonId FROM Task LEFT JOIN Person ON Task.PersonId = Person.Id WHERE Task.Status = 'TODO';"

        self.__cursor.execute(myQuery)

        rijen = self.__cursor.fetchall()

        print("---------------------")
        print("ALLE TAKEN")
        print("---------------------")

        df = pd.DataFrame(rijen,
        columns=['ID', 'Name', 'Status', 'Deadline', 'Priority', 'Description', 'PersonId'])

        df = df.fillna('None')
        pd.set_option('display.max_columns', None)
        pd.set_option('display.max_rows', None)
        print(df.to_string(index=False))

    def getAllTasksProgress(self):

        myQuery = "SELECT Task.Id, Task.Name, Task.Status, Task.Deadline, Task.Priority, Task.Description, PersonId FROM Task LEFT JOIN Person ON Task.PersonId = Person.Id WHERE Task.Status = 'IN_PROGRESS';"

        self.__cursor.execute(myQuery)

        rijen = self.__cursor.fetchall()

        print("---------------------")
        print("ALLE TAKEN")
        print("---------------------")

        df = pd.DataFrame(rijen,
        columns=['ID', 'Name', 'Status', 'Deadline', 'Priority', 'Description', 'PersonId'])

        df = df.fillna('None')
        pd.set_option('display.max_columns', None)
        pd.set_option('display.max_rows', None)
        print(df.to_string(index=False))

    def getAllTasksFinished(self):
        myQuery = "SELECT Task.Id, Task.Name, Task.Status, Task.Deadline, Task.Priority, Task.Description, PersonId FROM Task LEFT JOIN Person ON Task.PersonId = Person.Id WHERE Task.Status = 'FINISHED';"

        self.__cursor.execute(myQuery)

        rijen = self.__cursor.fetchall()

        print("---------------------")
        print("ALLE TAKEN")
        print("---------------------")

        df = pd.DataFrame(rijen,
                          columns=['ID', 'Name', 'Status', 'Deadline', 'Priority', 'Description', 'PersonId'])

        df = df.fillna('None')
        pd.set_option('display.max_columns', None)
        pd.set_option('display.max_rows', None)
        print(df.to_string(index=False))

    def getAllTasksNotFinished(self):
        myQuery = "SELECT Task.Id, Task.Name, Task.Status, Task.Deadline, Task.Priority, Task.Description, PersonId FROM Task LEFT JOIN Person ON Task.PersonId = Person.Id WHERE Task.Status != 'FINISHED';"

        self.__cursor.execute(myQuery)

        rijen = self.__cursor.fetchall()

        print("---------------------")
        print("ALLE TAKEN")
        print("---------------------")

        df = pd.DataFrame(rijen,
                          columns=['ID', 'Name', 'Status', 'Deadline', 'Priority', 'Description', 'PersonId'])

        df = df.fillna('None')
        pd.set_option('display.max_columns', None)
        pd.set_option('display.max_rows', None)
        print(df.to_string(index=False))


    def addTask(self, task):
        if not isinstance(task, Task):
            print("De meegegeven variabele is geen task")
        else:
            myQuery = "INSERT INTO Task (Name, Status, Deadline, Priority, Description) VALUES (?, ?, ?, ?, ?);"
            task_data = (task.get_name(), str(task.get_status().name), task.get_deadline(), str(task.get_priority()),
                         task.get_description())

            try:
                self.__cursor.execute(myQuery, task_data)
                self.__connection.commit()
            except sqlite3.Error as e:
                print(f"Fout bij het toevoegen van taak: {e}")
                self.__connection.rollback()

    def addPerson(self, person):
        if not isinstance(person, Person):
            print("De meegegeven variabele is geen person")
        else:
            myQuery = "INSERT INTO Person (Name,Birthday) VALUES (?,?);"
            person_data = (person.getName(), person.getBirthday())
            try:
                self.__cursor.execute(myQuery, person_data)
                self.__connection.commit()
            except sqlite3.Error as e:
                print(f"Fout bij het toevoegen van persoon: {e}")
                self.__connection.rollback()

    def removeTask(self, id):
        if self.doesTaskExist(id):
            myQuery = "DELETE FROM Task WHERE Id = ?;"
            self.__cursor.execute(myQuery, (id,))
            self.__connection.commit()
        else:
            print("Het opgegeven id bestaat niet\n")

    def removePerson(self, id):
        if self.doesPersonExist(id):
            myQuery = "DELETE FROM Person WHERE Id = ?;"
            self.__cursor.execute(myQuery, (id,))
            self.__connection.commit()
        else:
            print("Het opgegeven id bestaat niet\n")

    def doesTaskExist(self, task_id):
        myQuery = "SELECT COUNT(*) FROM Task WHERE Id = ?;"
        self.__cursor.execute(myQuery, (task_id,))
        result = self.__cursor.fetchone()

        # Als result[0] groter is dan 0, dan bestaat het ID
        return result[0] > 0

    def doesPersonExist(self, person_id):
        myQuery = "SELECT COUNT(*) FROM Person WHERE Id = ?;"
        self.__cursor.execute(myQuery, (person_id,))
        result = self.__cursor.fetchone()

        # Als result[0] groter is dan 0, dan bestaat het ID
        return result[0] > 0

    def getTaskId(self, name):
        myQuery = """SELECT Id FROM Task WHERE Name = ? ;"""
        self.__cursor.execute(myQuery, (name,))
        result = self.__cursor.fetchone()
        # print(result)
        return result[0]

    def getTaskById(self, id):
        myQuery = """SELECT * FROM Task WHERE Id = ? ;"""
        self.__cursor.execute(myQuery, (id,))
        result = self.__cursor.fetchone()
        return result

    def setNextStatusTask(self, id):
        if self.doesTaskExist(id):
            dbtaak = self.getTaskById(id)
            if dbtaak[2] == "IN_PROGRESS":
                taak = Task(dbtaak[1], TaskStatus.IN_PROGRESS, dbtaak[3], dbtaak[4], dbtaak[5])
            else:
                taak = Task(dbtaak[1], dbtaak[2], dbtaak[3], dbtaak[4], dbtaak[5])

            taak.set_next_status()
            print(taak.get_status())

            myQuery = "UPDATE Task SET Status = ? WHERE Id = ?;"
            self.__cursor.execute(myQuery, (taak.get_status().name, id))
            self.__connection.commit()

    def updateTaskPriority(self, id, new_priority):
        if self.doesTaskExist(id):
            dbtask = self.getTaskById(id)
            task = Task(dbtask[1], dbtask[2], dbtask[3], dbtask[4], dbtask[5])

            myQuery = "UPDATE Task SET Priority=? WHERE Id=?;"
            task_data = (new_priority, id)
            self.__cursor.execute(myQuery, task_data)
            self.__connection.commit()

    def updateTaskDeadline(self, id, new_deadline):
        if self.doesTaskExist(id):

            dbtask = self.getTaskById(id)
            task = Task(dbtask[1], dbtask[2], dbtask[3], dbtask[4], dbtask[5])

            myQuery = "UPDATE Task SET Deadline=? WHERE Id=?;"
            task_data = (new_deadline, id)
            self.__cursor.execute(myQuery, task_data)
            self.__connection.commit()

    def updateTaskPerson(self, taskId, personId):
        if self.doesTaskExist(taskId) and self.doesPersonExist(personId):
            dbtask = self.getTaskById(taskId)
            task = Task(dbtask[1], dbtask[2], dbtask[3], dbtask[4], dbtask[5])

            myQuery = "UPDATE Task SET PersonId=? WHERE Id=?;"
            task_data = (personId, taskId)
            self.__cursor.execute(myQuery, task_data)
            self.__connection.commit()
        else:
            print("PersonId or TaskId does not exist")
    def exportToExcel(self):
        query1 = "SELECT * FROM Task;"
        query2 = "SELECT * FROM Person"
        try:
            Tasks = pd.read_sql_query(query1, self.__connection)
            People = pd.read_sql_query(query2, self.__connection)

            excelfile = "output.xlsx"

            with pd.ExcelWriter(excelfile, engine='openpyxl') as writer:
                Tasks.to_excel(writer, sheet_name='Tasks', index=False)
                People.to_excel(writer, sheet_name='People', index=False)

            print("Gegevens succesvol geëxporteerd naar 'output.xlsx'")
        except Exception as e:
            print(f"Fout bij het exporteren naar Excel: {e}")
    def closeConnectionDb(self):
        self.__connection.close()
        print("Connectie met database gesloten")



if __name__ == '__main__':
    taak = Task("Naam", TaskStatus.TODO, "No deadline", 5, "beschrijving")
    db = DatabaseManager()
    # db.addTask(taak)
    db.getAllTasks()
    db.exportToExcel()
    # db.getAllPeople()
    # db.getTaskId("Clean")
    # db.getTaskByName("Clean")
    # db.setNextStatusTask("Clean")
    # db.updateTaskPriority("Clean",2)
