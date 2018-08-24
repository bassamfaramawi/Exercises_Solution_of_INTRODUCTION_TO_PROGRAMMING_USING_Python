''' 2.16 (Physics: acceleration) Average acceleration is defined as the change of velocity
          divided by the time taken to make the change, as shown in the following formula:
                       a = (v1 - v0) / t
     Write a program that prompts the user to enter the starting velocity in
     meters/second, the ending velocity in meters/second, and the time span t in
     seconds, and displays the average acceleration.


/**
 * @author BASSAM FARAMAWI
 * @email tiodaronzi3@yahoo.com
 * @since 2018
 */
'''
# Prompt the user for inputting the starting velocity, the ending velocity and the time span
v0, v1, t = eval(input("Enter v0, v1, and t: "))

# Compute the average acceleration
a = (v1 - v0) / t

# Display the result
print("The average acceleration is", int(a * 10000) / 10000)
