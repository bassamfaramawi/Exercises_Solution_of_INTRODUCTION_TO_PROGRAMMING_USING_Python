'''
*4.38 (Geometry: two rectangles) Write a program that prompts the user to enter the
center x-, y-coordinates, width, and height of two rectangles and determines
whether the second rectangle is inside the first or overlaps with the first, as shown
in Figure 4.15.

/**
 * @author BASSAM FARAMAWI
 * @email tiodaronzi3@yahoo.com
 * @since 2018
 */
'''
import turtle

# Prompt the user for entering r1's center x-, y-coordinates, width, and height
x1, y1, w1, h1 = eval(input("Enter r1's center x-, y-coordinates, width, and height: "))

# Prompt the user for entering r2's center x-, y-coordinates, width, and height
x2, y2, w2, h2 = eval(input("Enter r2's center x-, y-coordinates, width, and height: "))

turtle.penup()
turtle.goto(x1 - w1 / 2, y1 - h1 / 2)
turtle.pendown()
turtle.goto(x1 + w1 / 2, y1 - h1 / 2)
turtle.goto(x1 + w1 / 2, y1 + h1 / 2)
turtle.goto(x1 - w1 / 2, y1 + h1 / 2)
turtle.goto(x1 - w1 / 2, y1 - h1 / 2)
turtle.penup()
turtle.goto(x2 - w2 / 2, y2 - h2 / 2)
turtle.pendown()
turtle.goto(x2 + w2 / 2, y2 - h2 / 2)
turtle.goto(x2 + w2 / 2, y2 + h2 / 2)
turtle.goto(x2 - w2 / 2, y2 + h2 / 2)
turtle.goto(x2 - w2 / 2, y2 - h2 / 2)
turtle.penup()
turtle.goto(max(x1 + w1 / 2, x2 + w2 / 2) + 10, max(y1 + h1 / 2, y2 + h2 / 2) + 10)
turtle.pendown()

# r2 rectangle doesn't overlap r1 rectangle
if abs(max(x1, x2) - min(x1, x2)) > w1 + w2 and \
        abs(max(y1, y2) - min(y1, y2)) > h1 + h2:
    turtle.write("r2 does not overlap r1", font=("Arial", 20, "normal"))

# r2 rectangle is inside r1
elif abs(max(x1, x2) - min(x1, x2)) + (w2 / 2) <= w1 / 2 and \
        abs(max(y1, y2) - min(y1, y2)) + (h2 / 2) <= h1 / 2:
    turtle.write("r2 is inside r1", font=("Arial", 20, "normal"))

# r2 rectangle overlap r1 rectangle
else:
    turtle.write("r2 overlaps r1", font=("Arial", 20, "normal"))

turtle.hideturtle()  # Hide the turtle
turtle.done()  # Don't close the turtle graphics window
