'''
**5.18 (Find the factors of an integer) Write a program that
reads an integer and displays all its smallest factors, also
known as prime factors. For example, if the input integer is
120, the output should be as follows:
2, 2, 2, 3, 5

/**
 * @author BASSAM FARAMAWI
 * @email tiodaronzi3@yahoo.com
 * @since 2018
 */
'''
# Prompt the user to enter an integer
number = eval(input("Enter an integer: "))
n = 1  # Start count from after 1

print("The smallest factors for", str(number), "are:")

while n < number:
    n += 1
    if number % n != 0:
        continue  # If n is not a factor resume counting
    # Otherwise display the factor
    print(n, end="" if n == number else ", ")
    number /= n  # set the new number
    n = 1  # Reset counting
