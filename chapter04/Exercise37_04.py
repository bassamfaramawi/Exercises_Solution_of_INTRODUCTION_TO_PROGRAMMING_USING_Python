'''
**4.37 (Turtle: point in a rectangle?) Write a program that prompts the user to enter a
point (x, y) and checks whether the point is within the rectangle centered at (0,
0) with width 100 and height 50. Display the point, the rectangle, and a message
indicating whether the point is inside the rectangle in the window, as shown in
Figure 4.14.

/**
 * @author BASSAM FARAMAWI
 * @email tiodaronzi3@yahoo.com
 * @since 2018
 */
'''
import turtle

# Prompt the user to enter a point (x, y)
x, y = eval(input("Enter a point (x, y): "))

width = 100
height = 50

turtle.penup()
turtle.goto(-width / 2, -height / 2)
turtle.pendown()
turtle.goto(width / 2, -height / 2)
turtle.goto(width / 2, height / 2)
turtle.goto(-width / 2, height / 2)
turtle.goto(-width / 2, -height / 2)
turtle.penup()
turtle.goto(x, y)
turtle.pendown()
turtle.dot(6, "red")
turtle.penup()
turtle.goto(-width / 2 - 20, -height / 2 - 20)
turtle.pendown()

if x >= -width / 2 and x <= width / 2 and y >= -height / 2 and y <= height / 2:
    turtle.write("The point is inside the rectangle")
else:
    turtle.write("The point is not inside the rectangle")

turtle.hideturtle()  # Hide the turtle
turtle.done()  # Don't close the turtle graphics window
