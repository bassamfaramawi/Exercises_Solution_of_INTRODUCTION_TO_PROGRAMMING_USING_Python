'''
**1.18 (Turtle: draw a star) Write a program that draws a star, as shown in Figure 1.19c.
       (Hint: The inner angle of each point in the star is 36 degrees.)

/**
 * @author BASSAM FARAMAWI
 * @since 2018
 */
'''
# import turtle module
import turtle

# Use turtle module to draw the star
turtle.showturtle()

turtle.right(90 - (36.0 / 2))
turtle.forward(150)

turtle.right(180 - 36)
turtle.forward(150)

turtle.right(180 - 36)
turtle.forward(150)

turtle.right(180 - 36)
turtle.forward(150)

turtle.right(180 - 36)
turtle.forward(150)

turtle.done()
