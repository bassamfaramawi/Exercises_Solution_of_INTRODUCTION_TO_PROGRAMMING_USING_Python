'''
**4.21 (Science: day of the week) Zeller’s congruence is an algorithm developed by
Christian Zeller to calculate the day of the week. The formula is
where
■ h is the day of the week (0: Saturday, 1: Sunday, 2: Monday, 3: Tuesday,
4: Wednesday, 5: Thursday, 6: Friday).
■ q is the day of the month.
■ m is the month (3: March, 4: April, ..., 12: December). January and February are
counted as months 13 and 14 of the previous year.
■ j is the century (i.e., ).
■ k is the year of the century (i.e., year % 100).
Write a program that prompts the user to enter a year, month, and day of the
month, and then it displays the name of the day of the week.

/**
 * @author BASSAM FARAMAWI
 * @email tiodaronzi3@yahoo.com
 * @since 2018
 */
'''
# Asking for entering year
year = eval(input("Enter year: (e.g., 2012): "))

# Asking for entering m
m = eval(input("Enter month: 1-12: "))

# Convert input from 1 to 13 and from 2 to 14
if m == 1:
    m = 13
    year = year - 1
elif m == 2:
    m = 14
    year = year - 1

# Asking for entering day of the m
q = eval(input("Enter the day of the month: 1-31: "))

j = year // 100  # Compute the century
k = year % 100  # Compute the year of the century

# Calculate day of the week
h = (q + 26 * (m + 1) / 10 + k + k / 4 + j / 4 + 5 * j) % 7 // 1

# Display the result
print("Day of the week is", end=' ')

if h == 0:
    print("Saturday")
elif h == 1:
    print("Sunday")
elif h == 2:
    print("Monday")
elif h == 3:
    print("Tuesday")
elif h == 4:
    print("Wednesday")
elif h == 5:
    print("Thursday")
elif h == 6:
    print("Friday")
