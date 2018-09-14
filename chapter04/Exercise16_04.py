'''
4.16 (Random character) Write a program that displays a random uppercase letter.

/**
 * @author BASSAM FARAMAWI
 * @email tiodaronzi3@yahoo.com
 * @since 2018
 */
'''
import random

# Generate random ASCII of upper case letter
randomInt = random.randint(ord('A'), ord('Z'))

# Display the result
print(chr(randomInt))
