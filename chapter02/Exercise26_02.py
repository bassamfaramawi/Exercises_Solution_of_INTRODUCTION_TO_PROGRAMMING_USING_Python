''' **2.26 (Turtle: draw a circle) Write a program that prompts the user to enter the
            center and radius of a circle, and then displays the circle and its area.



/**
 * @author BASSAM FARAMAWI
 * @email tiodaronzi3@yahoo.com
 * @since 2018
 */
'''
import turtle  # Import turtle module
import math  # Import cmath module

# Prompt the user to enter center point
centerX, centerY = eval(input("Enter the circle center in X and Y: "))

# Prompt the user to enter the circle radius
radius = eval(input("Enter the circle radius: "))

turtle.showturtle()  # Show the turtle graphics window

# Draw circle
turtle.penup()
turtle.goto(centerX, centerY - radius)
turtle.pendown()
turtle.circle(radius)
turtle.penup()

# Write area inside circle
turtle.goto(centerX, centerY)
turtle.pendown()
area = math.pi * radius ** 2
turtle.write(int(area * 100) / 100)

turtle.done()  # Don't close the turtle graphics window
