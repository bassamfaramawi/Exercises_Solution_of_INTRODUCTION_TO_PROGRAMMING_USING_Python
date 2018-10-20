'''
**5.47 (Turtle: draw random balls) Write a program that displays 10 random balls in
a rectangle with width 120 and height 100, centered at (0, 0), as shown in
Figure 5.3a.

/**
 * @author BASSAM FARAMAWI
 * @email tiodaronzi3@yahoo.com
 * @since 2018
 */
'''
import random
import turtle

WIDTH = 120  # The square width
HEIGHT = 100  # The square height
diameter = 5  # The circle diameter

# Draw the square
turtle.penup()
turtle.goto(WIDTH / 2, HEIGHT / 2)
turtle.pendown()
turtle.color("black")
turtle.goto(-WIDTH / 2, HEIGHT / 2)
turtle.goto(-WIDTH / 2, -HEIGHT / 2)
turtle.goto(WIDTH / 2, -HEIGHT / 2)
turtle.goto(WIDTH / 2, HEIGHT / 2)

for i in range(10):
    # Generate the x and y coordinates
    x = WIDTH * (random.random() - 0.5)
    y = HEIGHT * (random.random() - 0.5)

    # draw the circles
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.dot(diameter, "red")

turtle.hideturtle()  # Hide the turtle
turtle.done()  # Don't close the turtle graphics window
