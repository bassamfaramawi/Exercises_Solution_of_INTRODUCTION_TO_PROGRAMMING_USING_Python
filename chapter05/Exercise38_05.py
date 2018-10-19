'''
*5.38 (Simulation: clock countdown) You can use the time.sleep(seconds) function
in the time module to let the program pause for the specified seconds. Write a
program that prompts the user to enter the number of seconds, displays a message
at every second, and terminates when the time expires.

/**
 * @author BASSAM FARAMAWI
 * @email tiodaronzi3@yahoo.com
 * @since 2018
 */
'''
from time import time

# Prompt the user to enter the number  of seconds
numberOfSeconds = eval(input("Enter the number of seconds: "))

# Calculate the time after the number of seconds
timeExpiration = int(time()) + numberOfSeconds
numberOfSeconds -= 1

# Use while loop to count seconds
while int(time()) < timeExpiration :
    if int(time()) == timeExpiration - numberOfSeconds :
        if numberOfSeconds > 0 :
            print(numberOfSeconds, "seconds remaining")
        else :
            break
        numberOfSeconds -= 1

print("Stopped") # Finish the counting