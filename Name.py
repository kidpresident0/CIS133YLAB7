#Name Module/Business Tier
#John Christian
from Database import Database


#Name Class/Constructor
class Name():
    def __init__(self, count, year, gender, name):
        self.__year = year
        self.__name = name
        self.__gender = gender
        self.__count = count

    # Getters
    @property
    def year(self):
        return self.__year

    @property
    def name(self):
        return self.__name

    @property
    def gender(self):
        return self.__gender

    @property
    def count(self):
        return self.__count

    # Setters
    @year.setter
    def year(self, new_year):
        self.__year = new_year

    @name.setter
    def name(self, new_name):
        self.__name = new_name

    @gender.setter
    def gender(self, new_gender):
        self.__gender = new_gender

    @count.setter
    def count(self, new_count):
        self.__name = new_count

    #Method for retrieving names from the Database and returning them to the main module.
    @staticmethod
    def getNames(year,gender):
        entries = []

        RowLst = Database.readNames(year, gender)
        for row in RowLst:
            entry = Name(row[0], row[1], row[2], row[3])
            entries.append(entry)

        return entries

