'''
**5.51 (Turtle: display a lattice) Write a program that displays an 18-by-18 lattice, as
shown in Figure 5.4c.

/**
 * @author BASSAM FARAMAWI
 * @email tiodaronzi3@yahoo.com
 * @since 2018
 */
'''
import turtle

SIDE = 180
step = SIDE / 18
x, y = 0, 0

# Draw the outer frame
turtle.goto(SIDE, y)
turtle.goto(SIDE, SIDE)
turtle.goto(x, SIDE)
turtle.goto(x, y)

# Draw the vertical lines
for n in range(1, 18):
    x += step
    turtle.penup()
    turtle.goto(x, 0)
    turtle.pendown()
    turtle.goto(x, SIDE)

# Draw the horizontal lines
for n in range(1, 18):
    y += step
    turtle.penup()
    turtle.goto(0, y)
    turtle.pendown()
    turtle.goto(SIDE, y)

turtle.hideturtle()  # Hide the turtle
turtle.done()  # Don't close the turtle graphics window
