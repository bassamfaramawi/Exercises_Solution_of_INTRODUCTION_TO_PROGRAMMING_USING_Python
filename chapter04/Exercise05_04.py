'''
*4.5 (Find future dates) Write a program that prompts the user to enter an integer for
today’s day of the week (Sunday is 0, Monday is 1, ..., and Saturday is 6). Also
prompt the user to enter the number of days after today for a future day and display
the future day of the week.

/**
 * @author BASSAM FARAMAWI
 * @email tiodaronzi3@yahoo.com
 * @since 2018
 */
'''
# Prompt the user to enter today's day
today = eval(input("Enter today's day: "))

if today >= 0 and today < 7:
    # Prompt the user to enter the number of days elapsed since today
    elapsed = eval(input("Enter the number of days elapsed since today: "))

    if today == 0:
        print("Today is Sunday", end='')
    elif today == 1:
        print("Today is Monday", end='')
    elif today == 2:
        print("Today is Tuesday", end='')
    elif today == 3:
        print("Today is Wednesday", end='')
    elif today == 4:
        print("Today is Thursday", end='')
    elif today == 5:
        print("Today is Friday", end='')
    elif today == 6:
        print("Today is Saturday", end='')

    # Compute the future day
    future = (today + elapsed) % 7;
    if future == 0:
        print(" and the future day is Sunday")
    elif future == 1:
        print(" and the future day is Monday")
    elif future == 2:
        print(" and the future day is Tuesday")
    elif future == 3:
        print(" and the future day is Wednesday")
    elif future == 4:
        print(" and the future day is Thursday")
    elif future == 5:
        print(" and the future day is Friday")
    elif future == 6:
        print(" and the future day is Saturday")

else:
    print("Invalid day number")
