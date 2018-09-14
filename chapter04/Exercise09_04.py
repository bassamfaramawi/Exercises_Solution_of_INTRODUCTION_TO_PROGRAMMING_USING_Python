'''
*4.9 (Financial: compare costs) Suppose you shop for rice and find it in two differentsized
packages. You would like to write a program to compare the costs of the
packages. The program prompts the user to enter the weight and price of each
package and then displays the one with the better price.

/**
 * @author BASSAM FARAMAWI
 * @email tiodaronzi3@yahoo.com
 * @since 2018
 */
'''
# Asking to enter weight and price or package 1
weight1, price1 = eval(input("Enter weight and price for package 1: "))

# Calculate the price of one of the first KG
priceOfKg1 = price1 / weight1

# Asking to enter weight and price for package 2
weight2, price2 = eval(input("Enter weight and price for package 2: "))

# Calculate the price of one of the second KG
priceOfKg2 = price2 / weight2

# Choose the cheapest price per kg
if priceOfKg1 < priceOfKg2:
    print("Package 1 has a better price.")
elif priceOfKg1 > priceOfKg2:
    print("Package 2 has a better price.")
else:
    print("Two packages have the same price.")
