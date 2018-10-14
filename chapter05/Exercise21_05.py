'''
**5.21 (Display numbers in a pyramid pattern) Write a nested for
loop that displays the following output:

/**
 * @author BASSAM FARAMAWI
 * @email tiodaronzi3@yahoo.com
 * @since 2018
 */
'''
for n in range(7 + 1):  # A for loop for printing the table
    for k in range(-7, 7 + 1):
        print(format(" " if abs(k) > n else str(int(pow(2, abs(abs(k) - n))))
                                            + "", ">4s"), end="")

    print()
