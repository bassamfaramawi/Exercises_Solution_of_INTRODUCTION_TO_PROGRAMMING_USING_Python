'''
   1.14 (Turtle: draw a triangle) Write a program that draws a triangle as shown in Figure 1.18c.

/**
 * @author BASSAM FARAMAWI
 * @since 2018
 */
'''
# import turtle module
import turtle

# Use turtle module to draw the traingle
turtle.showturtle()

turtle.penup()
turtle.goto(0, 50)

turtle.pendown()
turtle.goto(50, 0)
turtle.goto(-50, 0)
turtle.goto(0, 50)

turtle.done()
