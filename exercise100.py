# Write a function that determines how many days there are in a particular month. 

# Your function will take two parameters: 
# The month as an integer between 1 and 12, and the year as a four digit integer. 

# Ensure that your function reports the correct number of days in February for leap years. 

# Include a main program that reads a month and year from the user and displays the number of days in that month. 
# You may find your solution to Exercise 57 helpful when solving this problem.
days = {
    1 : 31,
    2 : 28,
    3 : 31,
    4 : 30,
    5 : 31,
    6 : 30,
    7 : 31,
    8 : 31,
    9 : 30,
    10 : 31,
    11 : 30,
    12 : 31
}
def NumofDays(month, year):
    day = 0
    for x in days:
        if (x == month and x != days[2]):
            day += days[x]
        elif ((x == month and month == days[2]) and year %4 != 0):
            day += days[x]
        elif ((x == month and month == days[2]) and year %4 == 0):
            day = 29
            return day
    print(day)
month = int(input("Please enter a month between 1-12: "))
year = int(input("Please enter a year in a four digit format (i.e. 2020): "))
NumofDays(month, year)