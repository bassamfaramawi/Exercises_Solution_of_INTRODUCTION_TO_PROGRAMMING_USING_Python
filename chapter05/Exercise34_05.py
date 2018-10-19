'''
**5.34 (Game: lottery) Revise Listing 4.10, Lottery.py, to generate a lottery of a two-digit
number. The two digits in the number are distinct. (Hint: Generate the first digit.
Use a loop to continuously generate the second digit until it is different from the
first digit.)

/**
 * @author BASSAM FARAMAWI
 * @email tiodaronzi3@yahoo.com
 * @since 2018
 */
'''
import random

# Generate the first digit of a lottery number
lotteryDigit1 = random.randint(0, 9)
lotteryDigit2 = lotteryDigit1  # Initialize the second digit

while lotteryDigit1 == lotteryDigit2:
    # Generate the first digit of a lottery number
    lotteryDigit2 = random.randint(0, 9)


# Prompt the user to enter a guess
guess = eval(input("Enter your lottery pick (two digits): "))

# Get digits from guess
guessDigit1 = guess / 10
guessDigit2 = guess % 10

print("The lottery number is " + str(lotteryDigit1) + str(lotteryDigit2))

# Check the guess
if guessDigit1 == lotteryDigit1 and guessDigit2 == lotteryDigit2:
    print("Exact match: you win $10,000")

elif guessDigit2 == lotteryDigit1 and guessDigit1 == lotteryDigit2:
    print("Match all digits: you win $3,000")

elif guessDigit1 == lotteryDigit1 or guessDigit1 == lotteryDigit2 \
    or guessDigit2 == lotteryDigit1 or guessDigit2 == lotteryDigit2:
    print("Match one digit: you win $1,000")

else:
    print("Sorry, no match")