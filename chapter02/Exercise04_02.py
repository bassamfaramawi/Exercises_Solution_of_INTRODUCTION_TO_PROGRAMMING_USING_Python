'''
 2.4 (Convert pounds into kilograms) Write a program that converts pounds into
      kilograms. The program prompts the user to enter a number in pounds, converts it
      to kilograms, and displays the result. One pound is 0.454 kilograms.

/**
 * @author BASSAM FARAMAWI
 * @email tiodaronzi3@yahoo.com
 * @since 2018
 */
'''

# Prompt the user for inputting number in pounds
pounds = eval(input("Enter a value in pounds: "))

# Compute kilograms
kilograms = pounds * 0.454

# Display results
print(pounds, "pounds is", kilograms, "kilograms")
