'''
**5.48 (Turtle: draw circles) Write a program that draws 10 circles with centers (0, 0), as
shown in Figure 5.3b.

/**
 * @author BASSAM FARAMAWI
 * @email tiodaronzi3@yahoo.com
 * @since 2018
 */
'''
import turtle
import random

# Circles will be drawn between 2 radius's
maxRadius = 200
minRadius = 100

for i in range(10):
    # Generate the current circle radius
    radius = minRadius + random.random() * (maxRadius - minRadius)
    # Draw the circle
    turtle.penup()
    turtle.goto(0, - radius)
    turtle.pendown()
    turtle.color("black")
    turtle.circle(radius)

turtle.hideturtle()  # Hide the turtle
turtle.done()  # Don't close the turtle graphics window
