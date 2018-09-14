'''
*4.20 (Science: wind-chill temperature) Exercise 2.9 gives a formula to compute the
wind-chill temperature. The formula is valid for temperatures in the range
between -58°F and 41°F and for wind speed greater than or equal to 2. Write a
program that prompts the user to enter a temperature and a wind speed. The program
displays the wind-chill temperature if the input is valid otherwise, it displays
a message indicating whether the temperature and/or wind speed is invalid.

/**
 * @author BASSAM FARAMAWI
 * @email tiodaronzi3@yahoo.com
 * @since 2018
 */
'''
# Asking for entering input
ta = eval(input("Enter the temperature in Fahrenheit between -58°F and 41°F: "))
v = eval(input("Enter the wind speed (>=2) in miles per hour: "))

if ta >= -58 and ta <= 41 and v >= 2:
    # Calculate the values
    twc = 35.74 + 0.6215 * ta - 35.75 * v ** 0.16 + 0.4275 * ta * v ** 0.16
    # Print the result
    print("The wind chill index is " + format(twc, ".5f"))
if ta < -58 or ta > 41:  # Check the temperature range
    print("The temperature is invalid")
if v < 2:  # Check the wind speed range
    print("The wind speed is invalid")
