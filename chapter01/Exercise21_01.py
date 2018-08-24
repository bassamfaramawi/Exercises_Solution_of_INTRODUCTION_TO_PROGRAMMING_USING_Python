'''
*1.21 (Turtle: display a clock) Write a program that displays a clock to show the time 9:15:00, as shown in Figure 1.20c.

/**
 * @author BASSAM FARAMAWI
 * @since 2018
 */
'''
# import turtle module
import turtle

# Use turtle module to draw the clock
turtle.showturtle()

turtle.penup()
turtle.goto(0, -100)
turtle.pendown()
turtle.circle(100)
turtle.penup()
turtle.goto(90, 0)
turtle.write(3)
turtle.goto(0, 85)
turtle.write(12)
turtle.goto(-96, 0)
turtle.write(9)
turtle.goto(0, -100)
turtle.write(6)
turtle.goto(-13, -115)
turtle.write("09:15:00")

turtle.goto(0, 0)
turtle.pendown()
turtle.backward(50)
turtle.forward(50)
turtle.left(90)
turtle.forward(70)
turtle.backward(70)
turtle.right(90)
turtle.forward(90)

turtle.done()
