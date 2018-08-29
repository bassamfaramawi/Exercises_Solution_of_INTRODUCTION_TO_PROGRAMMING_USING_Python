'''
**3.12 (Turtle: draw a star) Write a program that prompts the user to enter the length of
       the star and draw a star. (Hint: The inner angle of each point in the star is 36 degrees.)

/**
 * @author BASSAM FARAMAWI
 * @email tiodaronzi3@yahoo.com
 * @since 2018
 */
'''
import turtle  # Import turtle module

# Prompt the user to enter the length of the star
lenght = eval(input("Enter the length of the the star:"))

# Draw the star
turtle.forward(lenght)
turtle.right(180 - 36)

turtle.forward(lenght)
turtle.right(180 - 36)

turtle.forward(lenght)
turtle.right(180 - 36)

turtle.forward(lenght)
turtle.right(180 - 36)

turtle.forward(lenght)
turtle.right(180 - 36)

turtle.hideturtle()  # Hide the turtle

turtle.done()  # Don't close the turtle graphics window
