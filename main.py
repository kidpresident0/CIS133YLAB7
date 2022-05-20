#Lab 7
#John Christian
#CIS 133Y
#5/19/22
#This program collects user input for Year and Gender and returns the top 20
#names of people born in that year and a count of how many.It pulls that information
#from the United States Census SQL Database at PCC.
#Input: Year, Gender
#Ouput: Year, Name, Gender, Count
#Sources: Murach's Python Programming 2nd Addition, GitHub, Quora, Stack Overflow,
#W3 Schools, Week 7 Content, Week 7 Zoom Class.

#Main Module/User Tier

from Name import Name


#main function
def main():

    year = 0
    gender = ''
    lstNames = []


    ##Collects and validates user input for Gender and Year.
    while year not in range(1915, 2015):
        try:
            year = int(input("Enter the Year: "))
            print(year)
            if year not in range(1915, 2015):
                raise Exception
        except:
            print("Please enter a year between 1915 and 2015:")
    while gender != "M" or gender != "F":
        try:
            gender = str(input("Enter a Gender M/F: "))
            print(gender)
            if gender == "M" or gender == "F":
                break
            if gender != "M" or gender != "F":
                raise Exception
        except:
            print("Please enter M for Male or F for Female: ")

    #Declares the format for how the results will be displayed
    #and iterates through the list of values retrieved from Name module.
    lstNames = Name.getNames(year, gender)
    for entry in lstNames:
        print(f"{'Year:':7}{'Name:':15}{'Gender:':10}{'Count:':7}")

        entryLst = Name.getNames(year, gender)
        for entry in entryLst:
            print(f"{entry.year:<7}{entry.name:18}{entry.gender:3}{entry.count:11}")


main()





