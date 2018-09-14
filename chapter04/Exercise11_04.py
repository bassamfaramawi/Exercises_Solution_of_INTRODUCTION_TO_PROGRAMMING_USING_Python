'''
*4.11 (Find the number of days in a month) Write a program that prompts the user to
enter the month and year and displays the number of days in the month. For example,
if the user entered month 2 and year 2000, the program should display that
February 2000 has 29 days. If the user entered month 3 and year 2005, the program
should display that March 2005 has 31 days.

/**
 * @author BASSAM FARAMAWI
 * @email tiodaronzi3@yahoo.com
 * @since 2018
 */
'''
# Prompt the user to enter the month number
month = eval(input("Enter the month number: "))

# Prompt the user to the year
year = eval(input("Enter the year: "))

# compute the day in month and display the results
if month == 1:
    monthName = "January"
    monthDays = 31
    print(monthName, year, "had", monthDays, " days")
elif month == 2:
    monthName = "February"
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        monthDays = 29
    else:
        monthDays = 28
    print(monthName, year, "had", monthDays, "days")
elif month == 3:
    monthName = "March"
    monthDays = 31
    print(monthName, year, "had", monthDays, "days")
elif month == 4:
    monthName = "April"
    monthDays = 30
    print(monthName, year, "had", monthDays, "days")
elif month == 5:
    monthName = "May"
    monthDays = 31
    print(monthName, year, "had", monthDays, "days")
elif month == 6:
    monthName = "June"
    monthDays = 30
    print(monthName, year, "had", monthDays, "days")
elif month == 7:
    monthName = "July"
    monthDays = 31
    print(monthName, year, "had", monthDays, "days")
elif month == 8:
    monthName = "August"
    monthDays = 31
    print(monthName, year, "had", monthDays, "days")
elif month == 9:
    monthName = "September"
    monthDays = 30
    print(monthName, year, "had", monthDays, "days")
elif month == 10:
    monthName = "Otober"
    monthDays = 31
    print(monthName, year, "had", monthDays, "days")
elif month == 11:
    monthName = "November"
    monthDays = 30
    print(monthName, year, "had", monthDays, "days")
elif month == 12:
    monthName = "December"
    monthDays = 31
    print(monthName, year, "had", monthDays, "days")
else:
    print("Invalid month number.")
