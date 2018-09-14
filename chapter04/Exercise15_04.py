'''
**4.15 (Game: lottery) Revise Listing 4.10, Lottery.py, to generate a three-digit lottery
number. The program prompts the user to enter a three-digit number and determines
whether the user wins according to the following rules:
1. If the user input matches the lottery number in the exact order, the award is
$10,000.
2. If all the digits in the user input match all the digits in the lottery number, the
award is $3,000.
3. If one digit in the user input matches a digit in the lottery number, the award is
$1,000.
/**
 * @author BASSAM FARAMAWI
 * @email tiodaronzi3@yahoo.com
 * @since 2018
 */
'''
import random

# Generate a lottery number
lottery = random.randrange(0, 1000)

# Prompt the user to enter a guess
guess = eval(input("Enter your lottery pick (three digits): "))

# Get digits from lottery
lotteryDigit1 = lottery // 100
lotteryDigit2 = lottery % 100 // 10
lotteryDigit3 = lottery % 100 % 10

# Get digits from guess
guessDigit1 = guess // 100
guessDigit2 = guess % 100 // 10
guessDigit3 = guess % 100 % 10

print("The lottery number is", lottery)

# Check the guess
if guess == lottery:
    print("Exact match: you win $10,000")
elif ((guessDigit2 == lotteryDigit1) and (guessDigit1 == lotteryDigit2) and (guessDigit3 == lotteryDigit3)) or \
        ((guessDigit1 == lotteryDigit1) and (guessDigit3 == lotteryDigit2) and (guessDigit2 == lotteryDigit3)) or \
        ((guessDigit3 == lotteryDigit1) and (guessDigit1 == lotteryDigit2) and (guessDigit2 == lotteryDigit3)) or \
        ((guessDigit2 == lotteryDigit1) and (guessDigit3 == lotteryDigit2) and (guessDigit1 == lotteryDigit3)) or \
        ((guessDigit3 == lotteryDigit1) and (guessDigit2 == lotteryDigit2) and (guessDigit1 == lotteryDigit3)):
    print("Match all digits: you win $3,000")

elif ((guessDigit1 == lotteryDigit1) or (guessDigit1 == lotteryDigit2) or (guessDigit1 == lotteryDigit3) or \
      (guessDigit2 == lotteryDigit1) or (guessDigit2 == lotteryDigit2) or (guessDigit2 == lotteryDigit3) or \
      (guessDigit3 == lotteryDigit1) or (guessDigit3 == lotteryDigit2) or (guessDigit3 == lotteryDigit3)):
    print("Match one digit: you win $1,000")
else:
    print("Sorry, no match")
