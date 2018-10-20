'''
**5.54 (Turtle: plot the square function) Write a program that draws a diagram for the
function f(x) = x2 (see Figure 5.6a).

/**
 * @author BASSAM FARAMAWI
 * @email tiodaronzi3@yahoo.com
 * @since 2018
 */
'''
import turtle
import math

# Draw the horizontal axe
turtle.penup()
turtle.goto(-200, 0)
turtle.pendown()
turtle.goto(200, 0)
turtle.goto(190, 10)
turtle.penup()
turtle.goto(190, -10)
turtle.pendown()
turtle.goto(200, 0)

# Draw the vertical axe
turtle.penup()
turtle.goto(0, -100)
turtle.pendown()
turtle.goto(0, 100)
turtle.goto(10, 90)
turtle.penup()
turtle.goto(-10, 90)
turtle.pendown()
turtle.goto(0, 100)
turtle.penup()

turtle.color("red")
turtle.penup()
turtle.goto(0, 115)
turtle.pendown()
turtle.write("Y")
turtle.penup()

# Draw the square function
turtle.color("blue")
for x in range(-30, 31):
    turtle.goto(x, x * x)
    turtle.pendown()

turtle.hideturtle()  # Hide the turtle
turtle.done()  # Don't close the turtle graphics window
