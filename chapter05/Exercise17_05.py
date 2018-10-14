'''
*5.17 (Display the ASCII character table) Write a program that
displays the characters in the ASCII character table from ! to ~.
Display ten characters per line. The characters are separated by
exactly one space.

/**
 * @author BASSAM FARAMAWI
 * @email tiodaronzi3@yahoo.com
 * @since 2018
 */
'''
NUMBERS_PER_LINE = 10;  # Constant numbers per line
startASCII = ord('!');  # From the number
endASCII = ord('~');  # To the number

print("The ASCII table from ! to ~:")

for n in range(startASCII, endASCII + 1):
    # Display the result
    print(chr(n), end="\n" if (n - startASCII + 1) %
                              NUMBERS_PER_LINE == 0 else " ")
