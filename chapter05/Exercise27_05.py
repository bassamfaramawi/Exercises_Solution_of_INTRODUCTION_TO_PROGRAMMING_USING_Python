'''
**5.27 (Compute pi) You can approximate p by using the following series:
pi = 4(1 - 1/3 + 1/5 - 1/7 + 1/9 - 1/11 + g + -1^(i + 1)/(2i - 1)
≤
Write a program that displays the pi value for i = 10000, 20000, …, and
100000.

/**
 * @author BASSAM FARAMAWI
 * @email tiodaronzi3@yahoo.com
 * @since 2018
 */
'''
for n in range(10000, 100000, 10000):
    sum = 0
    print("PI for (n = " + str(n) + "): ", end="")

    for i in range(n, 0 - 1, -1):
        sum += (pow(-1, i + 1) / (2.0 * i - 1.0))

    PI = 4 * sum

    print(PI)
