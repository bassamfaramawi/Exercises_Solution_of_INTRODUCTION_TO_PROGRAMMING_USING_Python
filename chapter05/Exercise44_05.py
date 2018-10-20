'''
**5.44 (Decimal to binary) Write a program that prompts the user to enter a decimal integer
and displays its corresponding binary value.

/**
 * @author BASSAM FARAMAWI
 * @email tiodaronzi3@yahoo.com
 * @since 2018
 */
'''
# Prompt the user to enter integers
decimal = eval(input("Enter a decimal integer: "))

binary = ""  # Initialize the binary string
quotient = decimal  # Initialize the quotient

while quotient != 0:
    binary += "0" if quotient % 2 == 0 else "1"
    quotient = quotient // 2

# Display the binary value
print("The corresponding binary of", decimal, "is", binary)
