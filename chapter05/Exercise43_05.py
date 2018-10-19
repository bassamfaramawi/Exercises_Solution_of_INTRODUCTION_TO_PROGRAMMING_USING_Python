'''
*5.43 (Math: combinations) Write a program that displays all possible combinations for
picking two numbers from integers 1 to 7. Also display the total number of combinations.

/**
 * @author BASSAM FARAMAWI
 * @email tiodaronzi3@yahoo.com
 * @since 2018
 */
'''
count = 0  # Initialize count

for n in range(1, 7 + 1) :
    for i in range(n, 7 + 1) :
        if n == i : continue
        print(n, i)
        count += 1

# Display the result
print("The total number of all combinations is", count)