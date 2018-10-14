'''
**5.19 (Display a pyramid) Write a program that prompts the user
to enter an integer from 1 to 15 and displays a pyramid.

/**
 * @author BASSAM FARAMAWI
 * @email tiodaronzi3@yahoo.com
 * @since 2018
 */
'''
# Prompt the user to enter an integer from 1 to 15
number = eval(input("Enter an integer from 1 to 15: "))

for n in range(1, number + 1):  # A for loop for printing the table
    for k in range(-number, number + 1):
        print("  " if abs(k) > n else "" if k == 0 or k == 1
        else str(abs(k)) + " ", end="")

    print()
