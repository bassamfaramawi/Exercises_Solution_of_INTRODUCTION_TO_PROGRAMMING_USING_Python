'''
**5.55 (Turtle: chessboard) Write a program to draw a chessboard, as shown in
Figure 5.6b.

/**
 * @author BASSAM FARAMAWI
 * @email tiodaronzi3@yahoo.com
 * @since 2018
 */
'''
import turtle

step = 30
SIDE = 8 * step

# Draw the chessboard
for n in range(8):
    y = step * n
    for i in range(8):
        x = step * i
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        turtle.begin_fill()
        turtle.color("black" if (i + n) % 2 == 0 else "white")
        turtle.setheading(0)
        turtle.forward(step)
        turtle.left(90)
        turtle.forward(step)
        turtle.left(90)
        turtle.forward(step)
        turtle.left(90)
        turtle.forward(step)
        turtle.end_fill()

# Draw the outer frame
turtle.penup()
turtle.goto(0, 0)
turtle.color("black")
turtle.pendown()
turtle.goto(SIDE, 0)
turtle.goto(SIDE, SIDE)
turtle.goto(0, SIDE)
turtle.goto(0, 0)

turtle.hideturtle()  # Hide the turtle
turtle.done()  # Don't close the turtle graphics window
