'''
*4.32 (Geometry: point on line segment) Exercise 4.31 shows how to test whether a point
is on an unbounded line. Revise Exercise 4.31 to test whether a point is on a line
segment. Write a program that prompts the user to enter the x- and y-coordinates
for the three points p0, p1, and p2 and displays whether p2 is on the line segment
from p0 to p1.

/**
 * @author BASSAM FARAMAWI
 * @email tiodaronzi3@yahoo.com
 * @since 2018
 */
'''
# Asking to enter three points for p0, p1, and p2
x0, y0, x1, y1, x2, y2, = eval(input("Enter three points for p0, p1, and p2: "))

# Calculate the position
position = (x1 - x0) * (y2 - y0) - (x2 - x0) * (y1 - y0)

# point is on a line segment if position = 0 and x2 is between x0 and x1
if position == 0 and x2 >= min(x0, x1) and x2 <= max(x0, x1):
    print("(" + str(x2) + ", " + str(y2) + ") is on the line segment from (" + str(x0) +
          ", " + str(y0) + ") to (" + str(x1) + ", " + str(y1) + ")")

# Otherwise it is not on the line segment
else:
    print("(" + str(x2) + ", " + str(y2) + ") is not on the line segment from (" + str(x0)
          + ", " + str(y0) + ") to (" + str(x1) + ", " + str(y1) + ")")
