

class DateChecker:
    def __init__(self,datestring):
        self.__valid = False
        if not(len(datestring) == 10):
            print("Dit is geen geldige datum volgens het principe DD-MM-YYYY")
        else:
            day = int(datestring[0:2])
            month = int(datestring[3:5])
            year = int(datestring[6:10])
            if isinstance(day,int) and isinstance(month,int) and isinstance(year,int):
                #zeker getallen nu size check
                if 0 < day <= 31 and 0 < month <= 12 and year > 1900:
                    self.__day = day
                    self.__month = month
                    self.__year = year
                    self.__valid = True
                else:
                    print("De waarden in dag, maand of jaar kloppen niet")
            else:
                print("Jaar, Maand of dag is ongeldig")

    def getDate(self):
        return str(self.__day) + "-" + str(self.__month) + "-" + str(self.__year)

    def checkValid(self):
        return self.__valid


if __name__ == '__main__':
    string1 = "15-06-2000"
    datechecker = DateChecker(string1)
    print(datechecker.checkValid())