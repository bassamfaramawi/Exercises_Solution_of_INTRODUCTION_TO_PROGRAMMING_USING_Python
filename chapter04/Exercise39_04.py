'''
*4.39 (Turtle: two circles) Write a program that prompts the user to enter the center
coordinates and radii of two circles and determines whether the second circle is
inside the first or overlaps with the first, as shown in Figure 4.16.

/**
 * @author BASSAM FARAMAWI
 * @email tiodaronzi3@yahoo.com
 * @since 2018
 */
'''
import turtle

# Prompt the user to enter circle1's center x-, y-coordinates, and radius
x1, y1, r1 = eval(input("Enter circle1's center x-, y-coordinates, and radius: "))

# Prompt the user to enter circle2's center x-, y-coordinates, and radius
x2, y2, r2 = eval(input("Enter circle2's center x-, y-coordinates, and radius: "))

turtle.penup()
turtle.goto(x1, y1 - r1)
turtle.pendown()
turtle.circle(r1)
turtle.penup()
turtle.goto(x2, y2 - r2)
turtle.pendown()
turtle.circle(r2)
turtle.penup()
turtle.goto(x2 - r2 - 25, y2 - r2 - 25)
turtle.pendown()

# Calculate the distance between tow centers double
distance = ((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1)) ** 0.5

# Circle2(the smallest circle) is inside circle1
if distance <= abs(r1 - r2):
    turtle.write("circle2 is inside circle1", font=("Arial", 20, "normal"))

# Circle2 overlaps circle1
elif distance <= abs(r1 + r2):
    turtle.write("circle2 overlaps circle1", font=("Arial", 20, "normal"))

# otherwise circle2 does not overlap circle1
else:
    turtle.write("circle2 does not overlap circle1", font=("Arial", 20, "normal"))

turtle.hideturtle()  # Hide the turtle
turtle.done()  # Don't close the turtle graphics window
