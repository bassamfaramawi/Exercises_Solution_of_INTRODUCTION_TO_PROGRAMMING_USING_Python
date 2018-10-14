'''
 **5.30 (Display the first days of each month) Write a
 program that prompts the user to enter the year and
 first day of the year, and displays the first day of each
 month in the year. For example, if the user entered the year
 2013, and 2 for Tuesday, January 1, 2013, your program should
 display the following output:

     January 1, 2013 is Tuesday
     ...
     December 1, 2013 is Sunday

/**
 * @author BASSAM FARAMAWI
 * @email tiodaronzi3@yahoo.com
 * @since 2018
 */
'''
# Prompt the user to a year
year = eval(input("Enter a year: "))

# Prompt the user to enter the first day of year
firstDay = eval(input("Enter first day of the year (0 for Sunday, "
                      + " .. , 6 for Saturday): "))

dayOfWeek = ""  # Initialize day of week name
monthName = ""  # Initialize month name
monthDays = 0  # Initialize the number of month days

print("Year months first days:")

for n in range(1, 12 + 1):
    if n == 1:
        monthName = "January"
        monthDays = 31

    elif n == 2:
        monthName = "February"
        monthDays = 29 if year % 400 == 0 or \
                          (year % 4 == 0 and year % 100 != 0) else 28

    elif n == 3:
        monthName = "March"
        monthDays = 31

    elif n == 5:
        monthName = "May"
        monthDays = 31

    elif n == 7:
        monthName = "July"
        monthDays = 31

    elif n == 8:
        monthName = "August"
        monthDays = 31

    elif n == 10:
        monthName = "October"
        monthDays = 31

    elif n == 12:
        monthName = "December"
        monthDays = 31

    elif n == 4:
        monthName = "April"
        monthDays = 30

    elif n == 6:
        monthName = "June"
        monthDays = 30

    elif n == 9:
        monthName = "September"
        monthDays = 30

    elif n == 11:
        monthName = "November"
        monthDays = 30

    dayOfWeek = "Sunday" if firstDay == 0 else "Monday" if firstDay == 1 \
        else "Tuesday" if firstDay == 2 else "Wednesday" if firstDay == 3 \
        else "Thursday" if firstDay == 4 else "Friday" if firstDay == 5 \
        else "Saturday"

    print("  ", monthName, "1,", year, "is", dayOfWeek)

    # Shift to first day of next month
    firstDay = (firstDay + monthDays) % 7
