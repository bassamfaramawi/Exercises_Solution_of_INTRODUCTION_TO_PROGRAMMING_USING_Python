'''
*3.5 (Geometry: area of a regular polygon) A regular polygon is an n-sided polygon in
      which all sides are of the same length and all angles have the same degree (i.e., the
      polygon is both equilateral and equiangular). The formula for computing the area
      of a regular polygon is
         Area = n * s * s / (4 * math.tan(math.pi / n))
      Here, s is the length of a side. Write a program that prompts the user to enter the
      number of sides and their length of a regular polygon and displays its area.


/**
 * @author BASSAM FARAMAWI
 * @email tiodaronzi3@yahoo.com
 * @since 2018
 */
'''
import math  # Import cmath module

# Prompt the user to enter the number of sides of the pentagon
n = eval(input("Enter the number of sides:"))

# Prompt the user to enter the side of the pentagon
s = eval(input("Enter the side:"))

# Compute the area of the pentagon
area = n * s * s / (4 * math.tan(math.pi / n))

# Display the result
print("The area of the pentagon is", area)
