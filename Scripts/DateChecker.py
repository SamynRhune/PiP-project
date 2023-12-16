

class DateChecker:
    def __init__(self,datestring):
        self.__valid = False
        if not(len(datestring) == 10):
            print("Dit is geen geldige datum volgens het principe DD-MM-YYYY")
        else:
            day = datestring[0:2]
            month = datestring[3:5]
            year = datestring[6:10]
            if isinstance(day,int) and isinstance(month,int) and isinstance(year,int):
                #zeker getallen nu size check
                if 0 < day <= 31 and 0 < month <= 12 and year > 1900:
                    self.__day = day
                    self.__month = month
                    self.__year = year
                    self.__valid = True
            else:
                print("Jaar, Maand of dag is ongeldig")

    def getDate(self):
        return self.__day + "-" + self.__month + "-" + self.__year

    def checkValid(self):
        return self.__valid