'''
3.7 (Random character) Write a program that displays a random uppercase letter
     using the time.time() function.

/**
 * @author BASSAM FARAMAWI
 * @email tiodaronzi3@yahoo.com
 * @since 2018
 */
'''
import time  # Import time module

ascii = int(time.time() * 1000) % 128  # Generate random ascii code

print(chr(ascii).upper())  # Display its character
