import sqlite3
from Task import Task
from TaskStatus import TaskStatus
from Person import Person
import pandas as pd
import os


class DatabaseManager:
    def __init__(self):
        current_directory = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.join(current_directory, "..", "Databases", "TaskDatabase.db")
        self.__connection = sqlite3.connect(db_path)
        self.__cursor = self.__connection.cursor()

    def getAllTasks(self):
        myQuery = "SELECT Id,Name,Status,Deadline,Priority,Description,PersonId FROM Task"
        self.__cursor.execute(myQuery)

        rijen = self.__cursor.fetchall()

        print("All Tasks")
        print("------------------------")
        for rij in rijen:
            print(rij)

    def getAllPeople(self):
        myQuery = "SELECT Id,Name,Birthday FROM Person"
        self.__cursor.execute(myQuery)

        rijen = self.__cursor.fetchall()

        print("All People")
        print("------------------------")
        for rij in rijen:
            print(rij)

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
            self.__cursor.execute(myQuery, person_data)
            self.__connection.commit()

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
            taak = Task(dbtaak[1], dbtaak[2], dbtaak[3], dbtaak[4], dbtaak[5])
            taak.set_next_status()

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

            #TODO check if deadline is date

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
