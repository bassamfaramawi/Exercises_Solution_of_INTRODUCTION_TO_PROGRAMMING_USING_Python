'''
1.16 (Turtle: draw four circles) Write a program that draws four circles in the center of the screen,
     as shown in Figure 1.19a.

/**
 * @author BASSAM FARAMAWI
 * @since 2018
 */
'''
# import turtle module
import turtle

# Use turtle module to draw the four circles
turtle.showturtle()

turtle.penup()
turtle.goto(50, 50)
turtle.pendown()
turtle.circle(50)

turtle.penup()
turtle.goto(-50, 50)
turtle.pendown()
turtle.circle(50)

turtle.penup()
turtle.goto(-50, -50)
turtle.pendown()
turtle.circle(50)

turtle.penup()
turtle.goto(50, -50)
turtle.pendown()
turtle.circle(50)

turtle.done()
