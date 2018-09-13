'''
*4.1 (Algebra: solve quadratic equations) The two roots of a quadratic equation
         ax2 + bx + c = 0 can be obtained using the following formula:
                r1 = (-b + (b**2 - 4ac)**0.5) / 2a
            and r2 = (-b + (b**2 - 4ac)**0.5) / 2a
         b**2 - 4ac is called the discriminant of the quadratic equation. If it is
         positive, the equation has two real roots. If it is zero, the equation
         has one root. If it is negative, the equation has no real roots.
Write a program that prompts the user to enter values for a, b, and c and displays
the result based on the discriminant. If the discriminant is positive, display two
roots. If the discriminant is 0, display one root. Otherwise, display “The equation
has no real roots”.

/**
 * @author BASSAM FARAMAWI
 * @email tiodaronzi3@yahoo.com
 * @since 2018
 */
'''
# Prompt the user to enter a, b and c
a, b, c = eval(input("Enter a, b, c: "))

# Compute discriminant
discriminant = b * b - 4 * a * c

# 1'st if the discriminant is positive
if discriminant > 0:
    # Calculate the tow roots
    r1 = (-b + discriminant ** 0.5) / (2 * a)
    r2 = (-b - discriminant ** 0.5) / (2 * a)
    # Display the results
    print("The equation has two roots", r1, "and", r2)

# 2'nd if the discriminant = 0
elif discriminant == 0:
    # Calculate the root
    r1 = (-b + discriminant ** 0.5) / (2 * a)
    # Display the result
    print("The equation has one root", r1)

# 3'rd if the discriminant is negative
else:
    print("The equation has no real roots")  # No real roots
