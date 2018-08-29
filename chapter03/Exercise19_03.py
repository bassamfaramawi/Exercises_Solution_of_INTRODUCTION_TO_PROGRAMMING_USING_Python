'''
**3.19 (Turtle: draw a line) Write a program that prompts the user to enter two points
        and draw a line to connect the points and displays the coordinates of the points

/**
 * @author BASSAM FARAMAWI
 * @email tiodaronzi3@yahoo.com
 * @since 2018
 */
'''
import turtle  # Import turtle module

# Prompt the user to Enter 2 points
x1, y1, x2, y2 = eval(input("Enter tow points: "))

# Draw the line
turtle.penup()
turtle.goto(x1, y1)
turtle.pendown()
turtle.write("(" + str(x1) + ", " + str(y1) + ")")

turtle.goto(x2, y2)
turtle.write("(" + str(x2) + ", " + str(y2) + ")")

turtle.hideturtle()  # Hide the turtle
turtle.done()  # Don't close the turtle graphics window
