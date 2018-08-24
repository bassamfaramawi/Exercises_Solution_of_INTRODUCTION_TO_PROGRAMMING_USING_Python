'''
 *2.5 (Financial application: calculate tips) Write a program that reads the
       subtotal and the gratuity rate, then computes the gratuity and total. For
       example, if the user enters 10 for subtotal and 15% for gratuity rate, the
       program displays $1.5 as gratuity and $11.5 as

/**
 * @author BASSAM FARAMAWI
 * @email tiodaronzi3@yahoo.com
 * @since 2018
 */
'''

# Prompet the user for inputting the subtotal and a gratuity rate
subtotal, gratuityRate = eval(input("Enter the subtotal and a gratuity rate: "))

# Compute the subtotal and gratuityRate
gratuity = gratuityRate / 100.0 * subtotal
total = subtotal + gratuity

# Display results
print("The gratuity is", int(gratuity * 100) / 100, "and total is", int(total * 100) / 100)
