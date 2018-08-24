''' *2.13(Split digits) Write a program that prompts the user to enter a four-digit integer
          and displays the number in reverse order.


/**
 * @author BASSAM FARAMAWI
 * @email tiodaronzi3@yahoo.com
 * @since 2018
 */
'''

# Prompt the user for inputting a four-digit integer
integer = eval(input("Enter an integer: "))

# Compute thousands, hundreds, tens and odds
thousands = integer // 1000
remaining = integer % 1000

hundreds = remaining // 100
remaining = remaining % 100

tens = remaining // 10

odds = remaining % 10

# Display digits
print(thousands)
print(hundreds)
print(tens)
print(odds)
