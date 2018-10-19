'''
**5.41 (Occurrence of max numbers) Write a program that reads integers, finds the
largest of them, and counts its occurrences. Assume that the input ends with number
0. Suppose that you entered 3 5 2 5 5 5 0 the program finds that the
largest number is 5 and the occurrence count for 5 is 4. (Hint: Maintain two variables,
max and count. The variable max stores the current maximum number, and
count stores its occurrences. Initially, assign the first number to max and 1 to
count. Compare each subsequent number with max. If the number is greater than
max, assign it to max and reset count to 1. If the number is equal to max, increment
count by 1.)

/**
 * @author BASSAM FARAMAWI
 * @email tiodaronzi3@yahoo.com
 * @since 2018
 */
'''
#Prompt the user to enter numbers
number = eval(input("Enter numbers: "))

max = 1  # Initialize max
count = 0  # Initialize count

while number != 0 :
    number = eval(input("Enter numbers: "))
    if number > max :
        max = number
        count = 1
    elif number == max :
        count += 1

# Display the result
print("The largest number is", max)
print("The occurrence count of the largest number is", count)
