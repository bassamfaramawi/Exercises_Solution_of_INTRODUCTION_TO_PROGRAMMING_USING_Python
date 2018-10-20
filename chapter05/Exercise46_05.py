'''
**5.46 (Statistics: compute mean and standard deviation) In business applications, 
you are often asked to compute the mean and standard deviation of data. The mean is
simply the average of the numbers. The standard deviation is a statistic that tells
you how tightly all the various data are clustered around the mean in a set of data.
For example, what is the average age of the students in a class? How close are the
ages? If all the students are the same age, the deviation is 0.
Write a program that prompts the user to enter ten numbers, and displays the
mean and standard deviations of these numbers using the following formula:
       mean = Exi / n = (x1 + x2 + .. + xn) / n
       deviation = ( (E(xi^2) - E(xi)^2 / n) / (n -1))^ 0.5

/**
 * @author BASSAM FARAMAWI
 * @email tiodaronzi3@yahoo.com
 * @since 2018
 */
'''
from math import sqrt

# Prompt the user to enter ten numbers
print("Enter ten numbers: ")

n = 10  # Ten numbers

sumOfX = 0  # Initialize the summation of numbers
sumOfXSquare = 0  # Initialize the summation of square of numbers

for i in range(1, n + 1):  # Receive the 10 numbers
    x = eval(input())
    sumOfX += x
    sumOfXSquare += pow(x, 2)

# Calculate the mean and the standard deviation
mean = sumOfX / n

deviation = sqrt((sumOfXSquare - sumOfX * sumOfX / n) / (n - 1))

# Display the result
print("The mean is", mean)
print("The standard deviation is", int(deviation * 1E5) / 1E5)
