'''
5.15 (Find the largest n such that n^3 < 12,000) Use a while loop to find
the largest integer n such that n^3 is less than 12,000.

/**
 * @author BASSAM FARAMAWI
 * @email tiodaronzi3@yahoo.com
 * @since 2018
 */
'''
n = 0  # Initialize n

while n ** 3 < 12000:
    n += 1

# Display the rresult
print("The smallest number such that n^2 > 12000 is: " + str(n - 1))
