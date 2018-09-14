'''
**4.4 (Game: learn addition) Write a program that generates two integers under 100 and
prompts the user to enter the sum of these two integers. The program then reports
true if the answer is correct, false otherwise. The program is similar to Listing 4.1.

/**
 * @author BASSAM FARAMAWI
 * @email tiodaronzi3@yahoo.com
 * @since 2018
 */
'''
import random

# Generate tow random integers
random1 = random.randrange(0, 100)
random2 = random.randrange(0, 100)

# Prompt the user to enter the sum of integers
answer = eval(input("Enter the sum of " + str(random1) + " and " + str(random2) + ": "))

# Check the answer and display result
print(random1 + random2 == answer)
