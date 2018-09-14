'''
*4.31 (Geometry: point position) Given a directed line from point p0(x0, y0) to
p1(x1, y1), you can use the following condition to decide whether a point p2(x2,
y2) is on the left of the line, on the right, or on the same line:

                                              (> 0) p2 is on the left side of the line
(x1 - x0)*(y2 - y0) - (x2 - x0)*(y1 - y0)===  (= 0) p2 is on the same line
                                              (< 0) p2 is on the right side of the line


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

# If position value > 0 the point is on the left side
if position > 0:
    print("(" + str(x2) + ", " + str(y2) + ") is on the left side "
          + "of the line from (" + str(x0) + ", " + str(y0) +
          ") to (" + str(x1) + ", " + str(y1) + ")")

# If position value = 0 the point is on the same line
elif position == 0:
    print("(" + str(x2) + ", " + str(y2) + ") is on the line from ("
          + str(x0) + ", " + str(y0) + ") to (" + str(x1) + ", " +
          str(y1) + ")")

# If position value, 0 the point is on the right side
else:
    print("(" + str(x2) + ", " + str(y2) + ") is on the right side "
          + "of the line from (" + str(x0) + ", " + str(y0) +
          ") to (" + str(x1) + ", " + str(y1) + ")")
