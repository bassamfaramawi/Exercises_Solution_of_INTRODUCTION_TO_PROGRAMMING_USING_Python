'''
*4.34 (Hex to decimal) Write a program that prompts the user to enter a hex character
and displays its corresponding decimal integer.

/**
 * @author BASSAM FARAMAWI
 * @email tiodaronzi3@yahoo.com
 * @since 2018
 */
'''
# Prompt the user to enter a hex value(
hex = input("Enter a hex character: ")

# If the input isn't in (0 - 9), (a - f) or (A - F) range
if len(hex) != 1 or (ord(hex) > ord('F') and ord(hex) < ord('a')) or ord(hex) > ord('f'):
    print("Invalid input")
else:  # Otherwise display the decimal value
    # Display the result
    print("The decimal value is", end=' ')
    if hex == 'a' or hex == 'A':
        print("10")
    elif hex == 'b' or hex == 'B':
        print("11")
    elif hex == 'c' or hex == 'C':
        print("12")
    elif hex == 'd' or hex == 'D':
        print("13")
    elif hex == 'e' or hex == 'E':
        print("14")
    elif hex == 'f' or hex == 'F':
        print("15")
    else:
        print(hex)
