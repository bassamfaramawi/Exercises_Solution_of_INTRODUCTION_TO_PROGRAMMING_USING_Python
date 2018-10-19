'''
**5.35 (Perfect number) A positive integer is called a perfect number if it is
equal to the sum of all of its positive divisors, excluding itself. For example,
6 is the first perfect number because 6 = 3 + 2 + 1. The next is 28 = 14 + 7 + 4
+ 2 + 1. There are four perfect numbers less than 10,000. Write a program to find
all these four numbers.

/**
 * @author BASSAM FARAMAWI
 * @email tiodaronzi3@yahoo.com
 * @since 2018
 */
'''
print("The perfect numbers less than 10,000 are ")

for n in range(2, 10000 + 1):
    sum = 0
    for i in range(1, n):
        sum = sum + i if n % i == 0 else sum
    if n == sum:
        print(n, end=" ")
