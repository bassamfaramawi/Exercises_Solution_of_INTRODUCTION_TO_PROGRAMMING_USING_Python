'''
*3.6 (Find the character of an ASCII code) Write a program that receives an ASCII
      code (an integer between 0 and 127) and displays its character. For example,
      if the user enters 97, the program displays the character a.

/**
 * @author BASSAM FARAMAWI
 * @email tiodaronzi3@yahoo.com
 * @since 2018
 */
'''
# Prompt the user to enter an ASCII code
ascii = eval(input("Enter an ASCII code:"))

# Display the character
print("The character is", chr(ascii))
