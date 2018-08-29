'''
    (Geometry: area of a pentagon) The area of a pentagon can be computed using the
               following formula (s is the length of a side):
                    Area = 5 * s * s / (4 * math.tan(math.pi / 5))
               Write a program that prompts the user to enter the side of a pentagon
               and displays the area.

/**
 * @author BASSAM FARAMAWI
 * @email tiodaronzi3@yahoo.com
 * @since 2018
 */
'''
import math  # Import cmath module

# Prompt the user to enter the side of the pentagon
s = eval(input("Enter the side:"))

# Compute the area of the pentagon
area = 5 * s * s / (4 * math.tan(math.pi / 5))

# Display the result
print("The area of the pentagon is", area)
