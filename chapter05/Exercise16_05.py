'''
*5.16 (Compute the greatest common divisor) For Listing 5.8, another
solution to find the greatest common divisor of two integers n1 and n2
is as follows: First find d to be the minimum of n1 and n2, and then
check whether d, d - 1, d - 2, ..., 2, or 1 is a divisor for both n1
and n2 in this order. The first such common divisor is the greatest
common divisor for n1 and n2.

/**
 * @author BASSAM FARAMAWI
 * @email tiodaronzi3@yahoo.com
 * @since 2018
 */
'''
# Prompt the user to enter two integers
n1 = eval(input("Enter first integer: "))
n2 = eval(input("Enter second integer: "))

d = min(n1, n2)

for k in range(d, 1, -1):
    if n1 % k == 0 and n2 % k == 0:
        gcd = k
        break

# Display the result
print("The greatest common divisor for",
      n1, "and", n2, "is", gcd)
