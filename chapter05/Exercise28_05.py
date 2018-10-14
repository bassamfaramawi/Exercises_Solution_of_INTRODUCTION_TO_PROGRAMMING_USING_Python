'''
**5.28 (Compute e) You can approximate e using the following series:
          e = 1 + 1/1! + 1/2! + 1/3! + 1/4! + ... + 1/i!
Write a program that displays the e value for i = 10000, 20000, …, and
100000. (Hint: Because i! = i * (i - 1) * ... * 2 * 1, then
1/i! is 1 /(i(i - 1)!)
Initialize e and item to be 1 and keep adding a new item to e. The new
item is the previous item divided by i for i = 2, 3, 4, . . . .)

/**
 * @author BASSAM FARAMAWI
 * @email tiodaronzi3@yahoo.com
 * @since 2018
 */
'''
e = 1.0
item = 1.0
for i in range(2, 10000 + 1):
    item /= (i / 1.0)
    e += item
    if i % 10000 == 0:
        print("e for (n = " + str(i) + ") is: " + str(e))
