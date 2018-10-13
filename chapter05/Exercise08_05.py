'''
5.8 (Use the math.sqrt function) Write a program that prints
the following table using the sqrt function in the math module.
Number     Square Root
0          0.0000
2          1.4142
...
18         5.2426
20         5.4721

/**
 * @author BASSAM FARAMAWI
 * @email tiodaronzi3@yahoo.com
 * @since 2018
 */
'''
from math import sqrt

# Print the header
print(format("Number", "<12s"), "Square Root")

# Print the table body
for number in range(0, 22, 2):
    print(format(number, "<12d"),
          format(sqrt(number), "<.4f"))
