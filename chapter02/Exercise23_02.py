'''2.23 (Turtle: draw four circles) Write a program that prompts the user to enter the
         radius and draws four circles in the center of the screen.


/**
 * @author BASSAM FARAMAWI
 * @email tiodaronzi3@yahoo.com
 * @since 2018
 */
'''
import turtle  # Import turtle module

radius = eval(input("Enter the circle radius: "))  # Prompt the user to enter the radius

turtle.showturtle()  # Show the turtle graphics window

# 1'st circle
turtle.circle(radius)
turtle.penup()

# 2'nd circle
turtle.right(90)
turtle.forward(2 * radius)
turtle.pendown()
turtle.left(90)
turtle.circle(radius)
turtle.penup()

# 3'rd circle
turtle.backward(2 * radius)
turtle.pendown()
turtle.circle(radius)
turtle.penup()

# 4'th circle
turtle.left(90)
turtle.forward(2 * radius)
turtle.pendown()
turtle.right(90)
turtle.circle(radius)
turtle.penup()

turtle.done()  # Don't close the turtle graphics window
