'''
*3.3 (Algebra: solve 2 * 2 linear equations) A linear equation can be solved using
Cramer’s rule given in Programming Exercise 1.13. Write a program that prompts
the user to enter a, b, c, d, e, and f and displays the result. If ad - bc is 0, report
that “The equation has no solution.”
/**
 * @author BASSAM FARAMAWI
 * @email tiodaronzi3@yahoo.com
 * @since 2018
 */
'''
# Prompt the user to enter a, b, c, d, e and f
a, b, c, d, e, f = eval(input("Enter a, b, c, d, e, f: "))

if (a * d - b * c) == 0:  # The equation has no solution
    print("The equation has no solution")
else:  # Other than calculate x and y and display the results
    x = (e * d - b * f) / (a * d - b * c)
    y = (a * f - e * c) / (a * d - b * c)
    print("x is", x, "and y is", y)
