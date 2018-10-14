'''
*5.26 (Sum a series) Write a program to sum the following series:

      1/3 + 3/5 + 5/7 + 7/9 + 9/11 + 11/13 + ... + 95/97 + 97/99

/**
 * @author BASSAM FARAMAWI
 * @email tiodaronzi3@yahoo.com
 * @since 2018
 */
'''
n = 97  # The series count
sum = 0  # Initialize the summation

# Display the summation
print("The summation of the series 1/3 + ... + 97/99 is: ")
for i in range(1, n + 1, 2):
    sum += (i * 1.0 / (i + 2))
print(sum)
