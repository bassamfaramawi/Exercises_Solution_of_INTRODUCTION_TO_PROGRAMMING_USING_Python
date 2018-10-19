'''
5.40 (Simulation: heads or tails) Write a program that simulates flipping a coin
one million times and displays the number of heads and tails.

/**
 * @author BASSAM FARAMAWI
 * @email tiodaronzi3@yahoo.com
 * @since 2018
 */
'''
from random import randint

heads = 0  # Initialize the number of heads
tails = 0  # Initialize the number of tails

for n in range(1000000):
    # Randomly generate 0 for a head or 1 for a tail
    flip = randint(0, 1)

    if flip == 0 :
        heads  += 1
    else :
        tails  += 1

# Display the results
print("When flipping a coin one milion times, the number of :"
, "\nHeads =", heads, "\nTails =", tails)