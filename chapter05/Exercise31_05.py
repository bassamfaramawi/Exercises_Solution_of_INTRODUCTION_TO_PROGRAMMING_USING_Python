'''
**5.31 (Display calendars) Write a program that prompts the user to enter the
 year and first day of the year and displays the calendar table for the year on
 the console. For example, if the user entered the year 2013, and 2 for Tuesday,
 January 1, 2013, your program should display the calendar for each month in the
 year.

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

monthName = ""  # Initialize month name
monthDays = 0  # Initialize the number of month days

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

    # Print the header
    print("\n\n\n                 " + monthName + " " + str(year)
          + "\n____________________________________________________\n"
          + format("Sun", "<8s") + format("Mon", "<8s") + format("Tue", "<8s") +
          format("Wed", "<8s") + format("Thu", "<8s") + format("Fri", "<8s") +
          format("Sat", "<8s"))

    for i in range(firstDay):
        print(format("", "<8s"), end="")

    # Print the body of the month
    for i in range(1, monthDays + 1):
        print(format(i, "<8d"), end="\n" if (i + firstDay) % 7 == 0 else "")

    # Shift to the first day of the next month
    firstDay = (firstDay + monthDays) % 7
