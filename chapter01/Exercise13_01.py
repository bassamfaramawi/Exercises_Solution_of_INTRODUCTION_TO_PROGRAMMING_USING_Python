'''
1.13 (Turtle: draw a cross) Write a program that draws a cross as shown in Figure 1.18b

/**
 * @author BASSAM FARAMAWI
 * @since 2018
 */
'''
# import turtle module
import turtle

# Use turtle module to draw the cross
turtle.showturtle()

turtle.penup()
turtle.forward(50)

turtle.pendown()
turtle.backward(100)
turtle.penup()

turtle.left(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(50)

turtle.pendown()
turtle.right(90)
turtle.forward(100)

turtle.done()
