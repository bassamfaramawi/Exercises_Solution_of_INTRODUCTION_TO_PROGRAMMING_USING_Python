'''
3.14 (Turtle: draw the Olympic symbol ) Write a program that prompts the user to
      enter the radius of the rings and draws an Olympic symbol of five rings of the
      same size with the colors blue, black, red, yellow, and green

/**
 * @author BASSAM FARAMAWI
 * @email tiodaronzi3@yahoo.com
 * @since 2018
 */
'''
import turtle  # Import turtle module

# Prompts the user to enter the radius of the rings
radius = eval(input("Enter the radius of the rings:"))

# Set the space between centers
space = 2.25 * radius

# Draw the Olympic symbol
turtle.pensize(5)

turtle.color("blue")
turtle.circle(radius)
turtle.penup()

turtle.forward(space)
turtle.pendown()
turtle.color("black")
turtle.circle(radius)
turtle.penup()

turtle.forward(space)
turtle.pendown()
turtle.color("red")
turtle.circle(radius)
turtle.penup()

turtle.goto(space / 2, - space / 2)
turtle.pendown()
turtle.color("yellow")
turtle.circle(radius)
turtle.penup()

turtle.forward(space)
turtle.pendown()
turtle.color("green")
turtle.circle(radius)
turtle.penup()

turtle.hideturtle()  # Hide the turtle

turtle.done()  # Don't close the turtle graphics window
