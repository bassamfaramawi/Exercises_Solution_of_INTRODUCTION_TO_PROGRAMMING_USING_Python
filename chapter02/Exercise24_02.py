'''2.24 (Turtle: draw four hexagons) Write a program that draws four hexagons in the
         center of the screen.


/**
 * @author BASSAM FARAMAWI
 * @email tiodaronzi3@yahoo.com
 * @since 2018
 */
'''
import turtle  # Import turtle module

side = 30  # The hexagon side size

turtle.showturtle()  # Show the turtle graphics window

# 1'st hexagon
turtle.left(30)
turtle.forward(side)
turtle.left(60)
turtle.forward(side)
turtle.left(60)
turtle.forward(side)
turtle.left(60)
turtle.forward(side)
turtle.left(60)
turtle.forward(side)
turtle.left(60)
turtle.forward(side)
turtle.penup()

# 2'nd hexagon
turtle.pendown()
turtle.forward(side)
turtle.right(60)
turtle.forward(side)
turtle.right(60)
turtle.forward(side)
turtle.right(60)
turtle.forward(side)
turtle.right(60)
turtle.forward(side)
turtle.right(60)
turtle.forward(side)
turtle.penup()

# 3'rd hexagon
turtle.left(150)
turtle.forward(2 * side)
turtle.right(150)
turtle.pendown()
turtle.forward(side)
turtle.left(60)
turtle.forward(side)
turtle.left(60)
turtle.forward(side)
turtle.left(60)
turtle.forward(side)
turtle.left(60)
turtle.forward(side)
turtle.left(60)
turtle.forward(side)
turtle.penup()

# 4'th hexagon
turtle.pendown()
turtle.forward(side)
turtle.right(60)
turtle.forward(side)
turtle.right(60)
turtle.forward(side)
turtle.right(60)
turtle.forward(side)
turtle.right(60)
turtle.forward(side)
turtle.right(60)
turtle.forward(side)
turtle.penup()

turtle.done()  # Don't close the turtle graphics window
