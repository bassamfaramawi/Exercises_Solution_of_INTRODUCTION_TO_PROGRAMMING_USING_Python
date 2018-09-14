'''
4.14 (Game: heads or tails) Write a program that lets the user guess whether a flipped
coin displays the head or the tail. The program randomly generates an integer 0 or
1, which represents head or tail. The program prompts the user to enter a guess
and reports whether the guess is correct or incorrect.

/**
 * @author BASSAM FARAMAWI
 * @email tiodaronzi3@yahoo.com
 * @since 2018
 */
'''
import random

random = random.randint(0, 1)  # Generate random 0 or 1

# Prompt the user to enter to enter filing status
guess = eval(input("guess whether the flip of a coin results in" \
                   + "a head or a tail, 0 for head and 1 for tail: "))

# Check the if the guess is correct and diplay the result
print("Your guess is:", "Correct" if random == guess else "incorrect")
