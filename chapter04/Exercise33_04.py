'''
*4.33 (Decimal to hex) Write a program that prompts the user to enter an integer
between 0 and 15 and displays its corresponding hex number.

/**
 * @author BASSAM FARAMAWI
 * @email tiodaronzi3@yahoo.com
 * @since 2018
 */
'''
# Prompt the user to enter a decimal value(0 to 15)
decimal = eval(input("Enter a decimal value (0 to 15): "))

if decimal > 15 or decimal < 0:  # If the input isn't in (0 - 15) range
    print("Invalid input")
else:  # Otherwise display the hex value
    # Display the result
    print("The hex value is", end=' ')
    if decimal == 10:
        print("A")
    elif decimal == 11:
        print("B")
    elif decimal == 12:
        print("C")
    elif decimal == 13:
        print("D")
    elif decimal == 14:
        print("E")
    elif decimal == 15:
        print("F")
    else:
        print(decimal)
