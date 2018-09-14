'''
4.10 (Game: multiplication quiz) Listing 4.4, SubtractionQuiz.py, randomly generates
a subtraction question. Revise the program to randomly generate a multiplication
question with two integers less than 100.
/**
 * @author BASSAM FARAMAWI
 * @email tiodaronzi3@yahoo.com
 * @since 2018
 */
'''
import random

# 1. Generate two random single-digit integers
number1 = random.randrange(0, 100)
number2 = random.randrange(0, 100)

# 2. Prompt the student to answer "What is number1 - number2?"
answer = eval(input("What is " + str(number1) + " * " + str(number2) + "? "))

# 3. Check the answer and display the result
if number1 * number2 == answer:
    print("You are correct!")
else:
    print("Your answer is wrong.\n", number1, '*', number2, "is", number1 * number2, '.')
