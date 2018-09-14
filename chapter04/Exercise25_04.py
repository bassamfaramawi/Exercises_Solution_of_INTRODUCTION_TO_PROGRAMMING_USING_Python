'''
*4.25 (Geometry: intersecting point) Two points on line 1 are given as (x1, y1)
and (x2, y2) and on line 2 as (x3, y3) and (x4, y4), as shown in Figure 4.9a–b.
The intersecting point of the two lines can be found by solving the following
linear equation:
          (y1 - y2)x - (x1 - x2)y = (y1 - y2)x1 - (x1 - x2)y1
          (y3 - y4)x - (x3 - x4)y = (y3 - y4)x3 - (x3 - x4)y3
This linear equation can be solved using Cramer’s rule (see Programming Exercise
3.3). If the equation has no solutions, the two lines are parallel (Figure 3.8c).
Write a program that prompts the user to enter four points and displays the
intersecting point.

                  ax + by = e
                  cx + dy = f
                  x = (ed - bf) / (ad - bc)
                  y = (af - ec) / (ad - bc)

/**
 * @author BASSAM FARAMAWI
 * @email tiodaronzi3@yahoo.com
 * @since 2018
 */
'''
# Asking for ntering 4 points
x1, y1, x2, y2, x3, y3, x4, y4 = eval(input("Enter x1, y1, x2, " \
                                            "y2, x3, y3, x4, y4: "))

# Calculate a, b, c, d, e, f
a = y1 - y2
b = x1 - x2
c = y3 - y4
d = x3 - x4
e = (y1 - y2) * x1 - (x1 - x2) * y1
f = (y3 - y4) * x3 - (x3 - x4) * y3

# If parallel lines
if (a * d - b * c) == 0:
    print("The two lines are parallel")

# Otherwise calculate point coordinates and display the result
else:
    x = (e * d - b * f) / (a * d - b * c)
    y = (a * f - e * c) / (a * d - b * c)
    print("The intersecting point is at (" +
          format(x, ".4f") + ", " + format(y, ".4f") + ")")
