'''
*5.20 (Display four patterns using loops) Use nested loops that display the following
patterns in four separate programs:

        Pattern B
        1 2 3 4 5 6
        1 2 3 4 5
        1 2 3 4
        1 2 3
        1 2
        1

/**
 * @author BASSAM FARAMAWI
 * @email tiodaronzi3@yahoo.com
 * @since 2018
 */
'''
print("Pattern B")

for n in range(6, 0, -1):  # A for loop for printing the pattern
    for k in range(6 - n + 1, 6 + 1):
        print(k, end=" ")

    print()
