''' *2.14 (Geometry: area of a triangle) Write a program that prompts the user to enter the
           three points (x1, y1), (x2, y2), and (x3, y3) of a triangle and displays its area.
           The formula for computing the area of a triangle is
               s = (side1 + side2 + side3) / 2
               area = (2s(s - side1)(s - side2)(s - side3)) ** 0.5


/**
 * @author BASSAM FARAMAWI
 * @email tiodaronzi3@yahoo.com
 * @since 2018
 */
'''
# Prompet the user for inputting x1, y1, x2, y2, x3 and y3
x1, y1, x2, y2, x3, y3 = eval(input("Enter three points for a triangle: "))

# Compute the three sides
side1 = ((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)) ** 0.5
side2 = ((x2 - x3) * (x2 - x3) + (y2 - y3) * (y2 - y3)) ** 0.5
side3 = ((x3 - x1) * (x3 - x1) + (y3 - y1) * (y3 - y1)) ** 0.5

# Compute s
s = (side1 + side2 + side3) / 2

# Compute the area
area = (2 * s * (s - side1) * (s - side2) * (s - side3)) ** 0.5

# Display the result
print("The area of the triangle is ", int(area * 100) / 100)
