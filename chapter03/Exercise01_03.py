'''3.1 (Geometry: area of a pentagon) Write a program that prompts the user to enter the
       length from the center of a pentagon to a vertex and computes the area of the pentagon.
       The formula for computing the area of a pentagon is
                   Area =3 * 3 ** 0.5 / 2 * s ** 2
        where s is the length of a side.the length of a side. The side can be computed using the formula
                  s = 2 * r * sin(pi / 5)
       where r is the length from the center of a pentagon to a vertex.


/**
 * @author BASSAM FARAMAWI
 * @email tiodaronzi3@yahoo.com
 * @since 2018
 */
'''
import math  # Import cmath module

# Prompt the user to enter the length from the center to a vertex
r = eval(input("Enter the length from the center to a vertex: "))

# Compute the side length
s = 2 * r * math.sin(math.pi / 5)

# Compute the pentagon area
area = 3 * math.sqrt(3) / 2 * s ** 2

# Display the result
print("The area of the pentagon is ", format(area, "7.2f"))
