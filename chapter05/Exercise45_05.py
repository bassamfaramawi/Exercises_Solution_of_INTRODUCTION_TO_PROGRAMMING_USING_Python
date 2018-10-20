'''
**5.45 (Decimal to hex) Write a program that prompts the user to enter a decimal integer
and displays its corresponding hexadecimal value.

/**
 * @author BASSAM FARAMAWI
 * @email tiodaronzi3@yahoo.com
 * @since 2018
 */
'''
# Prompt the user to enter integers
decimal = eval(input("Enter a decimal integer: "))

hex = ""  # Initialize the hex string

quotient = decimal  # Initialize the quotient

while quotient != 0:
    hex += str(quotient % 16)
    quotient = quotient // 16

# Display the hex value
print("The corresponding octal of ", decimal, "is", hex)
