'''
**5.50 (Turtle: display numbers in a triangular pattern) Write a program that displays
numbers in a triangular pattern, as shown in Figure 5.4b.

/**
 * @author BASSAM FARAMAWI
 * @email tiodaronzi3@yahoo.com
 * @since 2018
 */
'''
import turtle

verticalSpace, horizontalSpace = 10, 10

for i in range(1, 10 + 1):
    y = - verticalSpace * i
    for n in range(1, i + 1):
        x = horizontalSpace * n
        turtle.penup()
        turtle.goto(x, y)
        turtle.write(n, font=("Arial", 8, "normal"))

turtle.hideturtle()  # Hide the turtle
turtle.done()  # Don't close the turtle graphics window
