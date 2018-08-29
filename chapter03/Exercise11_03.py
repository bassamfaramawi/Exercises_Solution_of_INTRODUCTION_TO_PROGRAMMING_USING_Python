'''
3.11 (Reverse number) Write a program that prompts the user to enter a four-digit integer
      and displays the number in reverse order.

/**
 * @author BASSAM FARAMAWI
 * @email tiodaronzi3@yahoo.com
 * @since 2018
 */
'''

# Prompt the user to enter a four-digit integer
number = eval(input("Enter an integer:"))

# Extract the four digits
firstDigit = int(number // 1e3)
remaining = number % 1e3
secondDigit = int(remaining // 1e2)
remaining = remaining % 1e2
thirdDigit = int(remaining // 1e1)
fourthDigit = int(remaining % 1e1)

# Display the integer in reverse order
print("The reversed number is " + str(fourthDigit) + str(thirdDigit) + str(secondDigit) + str(firstDigit))
