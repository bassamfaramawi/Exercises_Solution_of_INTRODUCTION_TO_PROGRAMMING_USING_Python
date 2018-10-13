'''
5.12 (Find numbers divisible by 5 and 6) Write a program that displays,
ten numbers per line, all the numbers from 100 to 1,000 that are divisible
by 5 and 6. The numbers are separated by exactly one space.

/**
 * @author BASSAM FARAMAWI
 * @email tiodaronzi3@yahoo.com
 * @since 2018
 */
'''
NUMBERS_PER_LINE = 10;  # Constant numbers per line
START_NUMBER = 100;  # From the number
END_NUMBER = 1000;  # To the number
count = 0;  # The count of numbers divisible by 5 & 6

print("The numbers divisible by 5 & 6 from", START_NUMBER,
      "to", END_NUMBER, "are: ")

for n in range(START_NUMBER, END_NUMBER + 1):
    if n % 5 == 0 and n % 6 == 0:
        count += 1
        # Display 10 number per line
        print(n, end="\n" if count % NUMBERS_PER_LINE == 0 else " ")
