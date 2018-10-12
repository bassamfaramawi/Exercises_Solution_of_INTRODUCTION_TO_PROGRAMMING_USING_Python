'''
5.2 (Repeat additions) Listing 5.4, SubtractionQuizLoop.py, generates five random
subtraction questions. Revise the program to generate ten random addition questions
for two integers between 1 and 15. Display the correct count and test time.

/**
 * @author BASSAM FARAMAWI
 * @email tiodaronzi3@yahoo.com
 * @since 2018
 */
'''
import random
import time

NUMBER_OF_QUESTIONS = 10  # Constant
count = 0  # Count the number of questions
correctCount = 0  # Count the number of correct answers

startTime = time.time()  # Get start time

while count < NUMBER_OF_QUESTIONS:
    # Generat tow integers between 1 and 15
    number1 = random.randint(1, 15)
    number2 = random.randint(1, 15)

    # Prompt the student to answer "What is number1 - number2?"
    answer = eval(input("What is " + str(number1) + " + " +
                        str(number2) + "? "))

    # Grade the answer and display the result
    if answer == number1 + number2:
        print("You are correct")
        correctCount += 1
    else:
        print("Your answer is wrong\n", number1, "+",
              number2, "=", (number1 + number2))

    # Increase the count
    count += 1

endTime = time.time()  # Get end time
testTime = int(endTime - startTime)  # Get test time

# Display the result
print("Correct count is", correctCount, "out of",
      NUMBER_OF_QUESTIONS, "\nTest time is", testTime, "seconds")
