'''
*3.15 (Turtle: paint a smiley face) Write a program that paints a smiley face.

/**
 * @author BASSAM FARAMAWI
 * @email tiodaronzi3@yahoo.com
 * @since 2018
 */
'''
import turtle  # Import turtle module

# Draw the smiley face
turtle.circle(100)

turtle.penup()
turtle.goto(40, 140)
turtle.pendown()
turtle.dot(30, "black")

turtle.penup()
turtle.goto(-40, 140)
turtle.pendown()
turtle.dot(30, "black")

turtle.penup()
turtle.goto(0, 125)
turtle.right(60)
turtle.pendown()
turtle.forward(70)

turtle.penup()
turtle.goto(0, 125)
turtle.right(60)
turtle.pendown()
turtle.forward(70)

turtle.penup()
turtle.goto(0, 40)
turtle.setheading(20)
turtle.pendown()
turtle.forward(70)

turtle.penup()
turtle.goto(0, 40)
turtle.setheading(180 - 20)
turtle.pendown()
turtle.forward(70)

turtle.hideturtle()  # Hide the turtle

turtle.done()  # Don't close the turtle graphics window
