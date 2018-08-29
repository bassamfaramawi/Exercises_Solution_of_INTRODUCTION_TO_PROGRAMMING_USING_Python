'''
*3.13 (Turtle: display a STOP sign) Write a program that displays a STOP sign.
       The hexagon is in red and the text is in white.

/**
 * @author BASSAM FARAMAWI
 * @email tiodaronzi3@yahoo.com
 * @since 2018
 */
'''
import turtle  # Import turtle module

radius = 70

# Draw the stop sign
turtle.hideturtle()
turtle.penup()
turtle.goto(- radius, 0)
turtle.pendown()
turtle.begin_fill()
turtle.color("red")
turtle.setheading(270)
turtle.circle(radius, steps=6)
turtle.end_fill()

turtle.penup()
turtle.goto(-40, -20)
turtle.pendown()
turtle.begin_fill()
turtle.color("white")
turtle.write("STOP", font=("Arial", 25, "normal"))

turtle.hideturtle()  # Hide the turtle

turtle.done()  # Don't close the turtle graphics window
