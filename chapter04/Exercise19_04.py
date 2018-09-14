'''
**4.19 (Compute the perimeter of a triangle) Write a program that reads three edges for a
triangle and computes the perimeter if the input is valid. Otherwise, display that
the input is invalid. The input is valid if the sum of every pair of two edges is
greater than the remaining edge.

/**
 * @author BASSAM FARAMAWI
 * @email tiodaronzi3@yahoo.com
 * @since 2018
 */
'''
# Prompt the user to enter 3 edges in cm
edge1, edge2, edge3 = eval(input("Enter the 3 edges in cm: "))

# Check if the input is valid and display the result
if (edge1 + edge2) > edge3 and (edge2 + edge3) > edge1 and (edge1 + edge3) > edge2:
    print("Perimeter = " + str(edge1 + edge2 + edge3))
else:
    print("The input is invalid.")
