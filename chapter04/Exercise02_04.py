'''
*4.2 (Game: add three numbers) The program in Listing 4.1 generates two integers and
prompts the user to enter the sum of these two integers. Revise the program to generate
three single-digit integers and prompt the user to enter the sum of these three
integers.

/**
 * @author BASSAM FARAMAWI
 * @email tiodaronzi3@yahoo.com
 * @since 2018
 */
'''
import random

# Generate random numbers
number1 = random.randint(0, 9)
number2 = random.randint(0, 9)
number3 = random.randint(0, 9)

# Prompt the user to enter an answer
answer = eval(input("What is " + str(number1) + " + " + str(number2) + " + " + str(number3) + "? "))

# Display result
print(number1, "+", number2, "+", number3, "=", answer, "is", number1 + number2 + number3 == answer)
