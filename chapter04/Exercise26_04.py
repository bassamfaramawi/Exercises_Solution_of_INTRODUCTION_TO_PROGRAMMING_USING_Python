'''
4.26 (Palindrome number) Write a program that prompts the user to enter a three-digit
integer and determines whether it is a palindrome number. A number is a palindrome
if it reads the same from right to left and from left to right.

/**
 * @author BASSAM FARAMAWI
 * @email tiodaronzi3@yahoo.com
 * @since 2018
 */
'''
# Prompt the user to enter a three-digit integer
number = eval(input("Enter a three-digit integer: "))

# Extract 1st and 3rd digits
digit1 = number // 100
digit2 = number % 100 // 10
digit3 = number % 10

# check if they are equal and display the result
print(number, "is", ("" if digit1 == digit3 else "not"), "a palindrome")
