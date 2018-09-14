'''
**4.22 (Geometry: point in a circle?) Write a program that prompts the user to enter a
point (x, y) and checks whether the point is within the circle centered at (0, 0)
with radius 10. For example, (4, 5) is inside the circle and (9, 9) is outside the
circle, as shown in Figure 4.8a.
(Hint: A point is in the circle if its distance to (0, 0) is less than or equal to 10.
The formula for computing the distance is 2(x2 - x1)2 + (y2 - y1)2. Test your
program to cover all cases.)

/**
 * @author BASSAM FARAMAWI
 * @email tiodaronzi3@yahoo.com
 * @since 2018
 */
'''
RADIUS = 10  # Assign the circle radius

# Asking for entering a point
x, y = eval(input("Enter a point with two coordinates: "))

# Calculate distance from (0, 0)
distance = (x * x + y * y) ** 0.5

# Check if in circle and display the result
print("Point (" + str(x) + ", " + str(y) + ") is " + \
      ("" if distance <= RADIUS else "not ") + "in the circle")
