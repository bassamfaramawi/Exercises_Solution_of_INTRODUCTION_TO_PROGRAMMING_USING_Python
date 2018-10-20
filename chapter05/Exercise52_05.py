'''
**5.52 (Turtle: plot the sine function) Write a program that plots the sine function, as
shown in Figure 5.5a.

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

# Draw the sine wave
for x in range(-175, 176):
    turtle.goto(x, 50 * math.sin((x / 100) * 2 * math.pi))
    turtle.pendown()

turtle.penup()
turtle.goto(-100, -15)
turtle.pendown()
turtle.write("-2\u03c0")
turtle.penup()
turtle.goto(100, -15)
turtle.pendown()
turtle.write("-2\u03c0")

turtle.hideturtle()  # Hide the turtle
turtle.done()  # Don't close the turtle graphics window
