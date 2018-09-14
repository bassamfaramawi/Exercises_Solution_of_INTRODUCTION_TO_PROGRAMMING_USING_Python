'''
*4.30 (Current time) Revise Programming Exercise 2.18 to display the hour using a 12-
hour clock.

/**
 * @author BASSAM FARAMAWI
 * @email tiodaronzi3@yahoo.com
 * @since 2018
 */
'''
import time

# Asking for entering input
GMT_Offset = eval(input("Enter the time zone offset to GMT: "))

# Calculate the values
totalSeconds = time.time() + GMT_Offset * 3600
hours = int(totalSeconds / 3600 % 24)
minutes = int(totalSeconds / 60 % 60)
seconds = int(totalSeconds % 60)

# Print the result
print("The current time is " + \
      # Display the hour using a 12 - hour clock
      (str(hours - 12) if hours > 12 else str(hours)) + ":" + str(minutes) + ":" + str(seconds))
