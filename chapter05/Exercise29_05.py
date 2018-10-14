'''
5.29 (Display leap years) Write a program that displays, ten per line,
all the leap years in the twenty-first century (from year 2001 to 2100).
The years are separated by exactly one space.

/**
 * @author BASSAM FARAMAWI
 * @email tiodaronzi3@yahoo.com
 * @since 2018
 */
'''
NUMBERS_PER_LINE = 10  # Years per one line
count = 0

print("The leap years between 101 and 2100:")

for n in range(101, 2100 + 1):
    if (n % 4 == 0 and n % 100 != 0) or n % 400 == 0:
        count += 1
        print(n, end="\n" if count % NUMBERS_PER_LINE == 0 else " ")
