'''
2.10 (Physics: finding runway length) Given an airplane’s acceleration a and
   take-off speed v, you can compute the minimum runway length needed for an
   airplane to take off using the following formula:
        length = v2 / 2a
   Write a program that prompts the user to enter v in meters/second (m/s) and
   the acceleration a in meters/second squared (m/s2), and displays the minimum
   runway length

/**
 * @author BASSAM FARAMAWI
 * @email tiodaronzi3@yahoo.com
 * @since 2018
 */
'''

# Prompt the user for  inpputting speed and acceleration:
speed, acceleration = eval(input("Enter speed and acceleration: "))

# Calculate length
length = speed ** 2 / (2 * acceleration)

# Display the results
print("The minimum runway length for this airplane is", int(length * 1000) / 1000)
