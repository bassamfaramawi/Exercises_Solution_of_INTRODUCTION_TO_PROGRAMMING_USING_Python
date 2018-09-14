'''
*4.8 (Sort three integers) Write a program that prompts the user to enter three integers
and displays them in increasing order.

/**
 * @author BASSAM FARAMAWI
 * @email tiodaronzi3@yahoo.com
 * @since 2018
 */
'''
# Prompt the user to enter integers
num1, num2, num3 = eval(input("Enter 3 integers: "))

# Make the necessary changes
if num1 > num2:
    temp = num1
    num1 = num2
    num2 = temp
if num2 > num3:
    temp = num2
    num2 = num3
    num3 = temp
if num1 > num2:
    temp = num1
    num1 = num2
    num2 = temp

# Display the results
print("The integers in non-decreasing order:", num1, num2, num3)
