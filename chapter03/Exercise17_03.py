'''
*3.17 (Turtle: triangle area) Write a program that prompts the user to enter the three
       points p1, p2, and p3 for a triangle and display its area below the triangle,.
       The formula for computing the area of a triangle is given
       in Exercise 2.14.

/**
 * @author BASSAM FARAMAWI
 * @email tiodaronzi3@yahoo.com
 * @since 2018
 */
'''
import turtle  # Import turtle module
import math  # Import cmath module

# Prompt the user to enter the three points p1, p2, and p3
x1, y1, x2, y2, x3, y3 = eval(input("Enter coordinates of the 3 points:"))

# draw the triangle
turtle.penup()
turtle.goto(x1, y1)
turtle.pendown()
turtle.write("p1(" + str(x1) + ", " + str(y1) + ")")
turtle.goto(x2, y2)
turtle.write("p2(" + str(x2) + ", " + str(y2) + ")")
turtle.goto(x3, y3)
turtle.write("p3(" + str(x3) + ", " + str(y3) + ")")
turtle.goto(x1, y1)

# Compute the three sides
side1 = math.sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2))
side2 = math.sqrt((x2 - x3) * (x2 - x3) + (y2 - y3) * (y2 - y3))
side3 = math.sqrt((x3 - x1) * (x3 - x1) + (y3 - y1) * (y3 - y1))

# Compute s
s = (side1 + side2 + side3) / 2

# Compute the area
area = math.sqrt(s * (s - side1) * (s - side2) * (s - side3))

turtle.penup()
turtle.goto(min(x1, x2, x3), min(y1, y2, y3) - 20)
turtle.pendown()
turtle.write("The area of the triangle is " + str(area))

turtle.hideturtle()  # Hide the turtle
turtle.done()  # Don't close the turtle graphics window
