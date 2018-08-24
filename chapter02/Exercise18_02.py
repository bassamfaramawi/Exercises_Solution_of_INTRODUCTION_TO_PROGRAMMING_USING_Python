'''2.18 (Current time) Listing 2.7, ShowCurrentTime.py, gives a program that displays the
           current time in GMT. Revise the program so that it prompts the user to enter the
           time zone in hours away from (offset to) GMT and displays the time in the specified
           time zone.



/**
 * @author BASSAM FARAMAWI
 * @email tiodaronzi3@yahoo.com
 * @since 2018
 */
'''

import time

# Prompt the user for inputting the time zone offset to GMT
timeOffset = eval(input("Enter the time zone offset to GMT: "))

currentTime = time.time()  # Get current time

# Obtain the total seconds since midnight, Jan 1, 1970
totalSeconds = int(currentTime) + 60 * 60 * timeOffset

currentSecond = totalSeconds % 60  # Get the current second

totalMinutes = totalSeconds // 60  # Obtain the total minutes

currentMinute = totalMinutes % 60  # Compute the current minute in the hour

totalHours = totalMinutes // 60  # Obtain the total hours

currentHour = totalHours % 24  # Compute the current hour

# Display the current time zone offset to GMT
print("The current time is", currentHour, ":", currentMinute, ":", currentSecond)
