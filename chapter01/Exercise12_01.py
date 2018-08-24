'''
   1.12 (Turtle: draw four squares) Write a program that draws four squares in the center of the screen,
        as shown in Figure 1.18a.

/**
 * @author BASSAM FARAMAWI
 * @since 2018
 */
'''

# import turtle module
import turtle

# Use turtle module to draw the four squares
turtle.showturtle()

turtle.forward(50)

turtle.left(90)
turtle.forward(50)

turtle.left(90)
turtle.forward(100)

turtle.left(90)
turtle.forward(100)

turtle.left(90)
turtle.forward(100)

turtle.left(90)
turtle.forward(50)

turtle.left(90)
turtle.forward(100)

turtle.penup()
turtle.backward(50)
turtle.left(90)

turtle.pendown()
turtle.forward(50)

turtle.penup()
turtle.backward(100)

turtle.pendown()
turtle.forward(50)

turtle.done()
