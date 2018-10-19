'''
*5.37 (Summation) Write a program to compute the following summation.
         1/(1 + 2^0.5) + 1/(2^0.5 + 3^0.5) + 1/(3^0.5 + 4^0.5) + ...
         + 1/(624^0.5 + 625^0.5)

/**
 * @author BASSAM FARAMAWI
 * @email tiodaronzi3@yahoo.com
 * @since 2018
 */
'''
from math import sqrt

sum = 0  # Initialize the summation

for n in range(1, 625):
    sum += (1.0 / (sqrt(n) + sqrt(n + 1)))

# Display the summation
print("The summation is:", sum)