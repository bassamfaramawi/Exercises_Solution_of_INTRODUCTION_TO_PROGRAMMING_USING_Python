''' **2.25 (Turtle: draw a rectangle) Write a program that prompts the user to enter the
           center of a rectangle, width, and height, and displays the rectangle.

/**
 * @author BASSAM FARAMAWI
 * @email tiodaronzi3@yahoo.com
 * @since 2018
 */
'''
import turtle  # Import turtle module

# Prompt the user to enter center point
centerX, centerY = eval(input("Enter the rectangle center X and Y: "))

# Prompt the user to enter width and height
width, height = eval(input("Enter the rectangle width and height: "))

turtle.showturtle()  # Show the turtle graphics window

# Draw the rectangle
turtle.penup()
turtle.goto(centerX - (width / 2), centerY - (height / 2))
turtle.pendown()
turtle.goto(centerX + (width / 2), centerY - (height / 2))
turtle.goto(centerX + (width / 2), centerY + (height / 2))
turtle.goto(centerX - (width / 2), centerY + (height / 2))
turtle.goto(centerX - (width / 2), centerY - (height / 2))

turtle.done()  # Don't close the turtle graphics window
