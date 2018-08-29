'''
**3.16 (Turtle: draw shapes) Write a program that draws a triangle, square, pentagon,
        hexagon, and octagon. Note that the bottom edges of these shapes are parallel
        to the x-axis. (Hint: For a triangle with a bottom line parallel to the x-axis,
        set the turtle’s heading to 60 degrees.)

/**
 * @author BASSAM FARAMAWI
 * @email tiodaronzi3@yahoo.com
 * @since 2018
 */
'''
import turtle  # Import turtle module

radius = 50  # The circle radius

# Draw the shape
turtle.penup()
turtle.goto(- radius * 4, 0)
turtle.pendown()
turtle.begin_fill()
turtle.color("red")
turtle.setheading(60)
turtle.circle(radius, steps=3)
turtle.end_fill()

turtle.penup()
turtle.goto(-radius * 2, 0)
turtle.pendown()
turtle.begin_fill()
turtle.color("blue")
turtle.setheading(45)
turtle.circle(radius, steps=4)
turtle.end_fill()

turtle.penup()
turtle.goto(0, 0)
turtle.pendown()
turtle.begin_fill()
turtle.color("black")
turtle.setheading(180 / 5)
turtle.circle(radius, steps=5)
turtle.end_fill()

turtle.penup()
turtle.goto(radius * 2, 0)
turtle.pendown()
turtle.begin_fill()
turtle.color("green")
turtle.setheading(180 / 6)
turtle.circle(radius, steps=6)
turtle.end_fill()

turtle.penup()
turtle.goto(radius * 4, 0)
turtle.pendown()
turtle.begin_fill()
turtle.color("yellow")
turtle.setheading(180 / 7)
turtle.circle(radius, steps=7)
turtle.end_fill()

turtle.hideturtle()  # Hide the turtle

turtle.done()  # Don't close the turtle graphics window
