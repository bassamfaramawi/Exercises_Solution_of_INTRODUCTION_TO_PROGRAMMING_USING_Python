'''
**4.23 (Geometry: point in a rectangle?) Write a program that prompts the user to enter
a point (x, y) and checks whether the point is within the rectangle centered at
(0, 0) with width 10 and height 5. For example, (2, 2) is inside the rectangle and
(6, 4) is outside the rectangle, as shown in Figure 4.8b. (Hint: A point is in the
rectangle if its horizontal distance to (0, 0) is less than or equal to 10 / 2 and
its vertical distance to (0, 0) is less than or equal to 5.0 / 2. Test your program
to cover all cases.)

/**
 * @author BASSAM FARAMAWI
 * @email tiodaronzi3@yahoo.com
 * @since 2018
 */
'''
# Assign the rectangle width and height
WIDTH = 10.0
HEIGHT = 5.0

# Asking for entering a point
x, y = eval(input("Enter a point with two coordinates: "))

# Check if in the point inside the rectangle and display the result
print("Point (" + str(x) + ", " + str(y) + ") is " + \
      ("" if x <= WIDTH / 2 and y <= HEIGHT / 2 else "not ") + \
      "in the rectangle")
