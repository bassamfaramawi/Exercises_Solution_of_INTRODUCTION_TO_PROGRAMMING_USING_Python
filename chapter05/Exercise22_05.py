'''
*5.22 (Display prime numbers between 2 and 1,000) Modify Listing
5.13 to display all the prime numbers between 2 and 1,000, inclusive.
Display eight prime numbers per line.

/**
 * @author BASSAM FARAMAWI
 * @email tiodaronzi3@yahoo.com
 * @since 2018
 */
'''
NUMBER_OF_PRIMES_PER_LINE = 8  # Display 8 per line
count = 0  # Count the number of prime numbers
number = 2  # A number to be tested for primeness

print("The prime numbers between 2 and 1000 are:")

# Repeatedly find prime numbers
while number <= 1000:
    # Assume the number is prime
    isPrime = True  # Is the current number prime?

    # Test whether number is prime
    for divisor in range(2, number // 2 + 1):
        if number % divisor == 0:  # If true, number is not prime
            isPrime = False  # Set isPrime to false
            break  # Exit the for loop

    # Display the prime number and increase the count
    if isPrime:
        count += 1  # Increase the count

        if count % NUMBER_OF_PRIMES_PER_LINE == 0:
            # Display the number and advance to the new line
            print(number)
        else:
            print(number, end=" ")
    # Check if the next number is prime
    number += 1
