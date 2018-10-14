'''
*5.20 (Display four patterns using loops) Use nested loops that display the following
patterns in four separate programs:

            Pattern C
                      1
                    2 1
                  3 2 1
                4 3 2 1
              5 4 3 2 1
            6 5 4 3 2 1

/**
 * @author BASSAM FARAMAWI
 * @email tiodaronzi3@yahoo.com
 * @since 2018
 */
'''
print("Pattern C")

for n in range(1, 6 + 1):  # A for loop for printing the pattern
    for k in range(6, 0, -1):
        print(" " if k > n else k, end=" ")

    print()
