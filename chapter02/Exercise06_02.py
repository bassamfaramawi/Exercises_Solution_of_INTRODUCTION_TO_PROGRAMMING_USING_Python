'''
 **2.6 (Sum the digits in an integer) Write a program that reads an integer
       between 0 and 1000 and adds all the digits in the integer. For example,
       if an integer is 932, the sum of all its digits is 14.
      Hint: Use the % operator to extract digits, and use the // operator to
      remove the extracted digit. For instance, 932 % 10 = 2 and 932 // 10 = 93.

/**
 * @author BASSAM FARAMAWI
 * @email tiodaronzi3@yahoo.com
 * @since 2018
 */
'''

# Prompt the user for inputting the number
number = eval(input("Enter a number between 0 and 1000: "))

# compute the digits
hundreds = number // 100
tens = number % 100 // 10
ones = number % 10

# Display results
print("The sum of the digits is", hundreds + tens + ones)
