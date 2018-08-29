'''
  2.1 (Convert Celsius to Fahrenheit) Write a program that reads a Celsius
       degree in a double value from the console, then converts it to Fahrenheit and
       displays the result. The formula for the conversion is as follows:
       fahrenheit = (9 / 5) * celsius + 32

/**
 * @author BASSAM FARAMAWI
 * @email tiodaronzi3@yahoo.com
 * @since 2018
 */
'''
# Prompt the user for inputting Celsuis degree
celsius = eval(input("Enter a degree in Celsius: "))

# Compute Fahrenheit degree
fahrenheit = 9 / 5 * celsius + 32

# Display result
print(celsius, "Celsius is", fahrenheit, "Fahrenheit")
