#Database Module/Data Tier
#John Christian

#Databass/Storage (temporarily a dictionary list of people named John from 1915-1919.)
import pyodbc




class Database:

    __connection = None

    #method for connecting to SQL databse
    @classmethod
    def connect(cls):
        if cls.__connection is None:
            server = 'tcp:cisdbss.pcc.edu'
            database = 'NAMES'
            username = '275student'
            password = '275student'
            cls.__connection = pyodbc.connect(
                'DRIVER={ODBC Driver 18 for SQL Server};SERVER=' + server
                + ';Encrypt=YES;TrustServerCertificate=YES'
                + ';DATABASE=' + database
                + ';UID=' + username + ';PWD=' + password
            )
    #SQL Query method that retrieves the data from the database and returns
    #it to Names
    @classmethod
    def readNames(cls, year, gender):

        cls.connect()
        lstNames = []
        cursor = cls.__connection.cursor()
        cursor = cls.__connection.cursor()
        query = '''
                SELECT TOP 20
                    name_counts.NameCount,
                    year_gender_totals.Year, year_gender_totals.Gender,
                    names.Name
                FROM name_counts
                JOIN year_gender_totals
                    ON year_gender_totals.YearGenderTotalID =
                    name_counts.FK_YearGenderTotalID
                JOIN names
                    ON names.NameID = name_counts.FK_NameID
                WHERE year_gender_totals.Year = ?
                AND year_gender_totals.Gender = ?
                ORDER BY name_counts.NameCount DESC
                '''

        cursor.execute(query, (year, gender))
        myRows = cursor.fetchall()

        return myRows



