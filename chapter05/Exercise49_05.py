'''
**5.49 (Turtle: display a multiplication table) Write a program that displays a multiplication
table, as shown in Figure 5.4a.

/**
 * @author BASSAM FARAMAWI
 * @email tiodaronzi3@yahoo.com
 * @since 2018
 */
'''
import turtle

horizontalSpace = 20
verticalSpace = 20

# Print the table header
turtle.penup()
x = horizontalSpace
y = 3 * verticalSpace
turtle.goto(x, y)
turtle.pendown()
turtle.write("Multiplication Table", font=("Arial", 12, "normal"))

# Print the horizontal numbers
y = y - verticalSpace
for i in range(1, 10):
    turtle.penup()
    x = i * horizontalSpace
    turtle.goto(x, y)
    turtle.pendown()
    turtle.write(format(i, "<4d"), font=("Arial", 8, "normal"))

# Print the vertical numbers
turtle.penup()
y = y - verticalSpace
x = x - horizontalSpace

for i in range(-1, 10):
    turtle.penup()
    x = i * horizontalSpace
    turtle.goto(x, y)
    turtle.pendown()
    turtle.write(" - - - ", font=("Arial", 8, "normal"))

# Print the table body
for i in range(1, 10):
    turtle.penup()
    y = y - verticalSpace
    x = - horizontalSpace
    turtle.goto(x, y)
    turtle.pendown()
    turtle.write(format(i, "<4d") + format("|", "<4s"),
                 font=("Arial", 8, "normal"))
    for n in range(1, 10):
        turtle.penup()
        x = n * horizontalSpace
        turtle.goto(x, y)
        turtle.pendown()
        turtle.write(n * i, font=("Arial", 8, "normal"))

turtle.hideturtle()  # Hide the turtle
turtle.done()  # Don't close the turtle graphics window
