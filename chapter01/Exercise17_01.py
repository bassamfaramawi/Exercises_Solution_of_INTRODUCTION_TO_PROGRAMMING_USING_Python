'''
1.17 (Turtle: draw a line) Write a program that draws a red line connecting two points (-39, 48) and (50, -50) and
displays the coordinates of the two points, as shown in Figure 1.19b.

/**
 * @author BASSAM FARAMAWI
 * @since 2018
 */
'''
# import turtle module
import turtle

# Use turtle module to draw the line connecting tow points
turtle.showturtle()
turtle.penup()

turtle.goto(-39, 48)
turtle.write("(-39, 48)")

turtle.pendown()
turtle.goto(50, -50)
turtle.write("(50, -50)")

turtle.done()
