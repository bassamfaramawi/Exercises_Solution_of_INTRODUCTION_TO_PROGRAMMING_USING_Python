'''
4.7 (Financial application: monetary units) Modify Listing 3.4, ComputeChange.py,
to display the nonzero denominations only, using singular words for single units
such as 1 dollar and 1 penny, and plural words for more than one unit such as 2
dollars and 3 pennies.
/**
 * @author BASSAM FARAMAWI
 * @email tiodaronzi3@yahoo.com
 * @since 2018
 */
'''
# Prompt the user to enter an amount
amount = eval(input("Enter an amount in double, for example 11.56: "))

remainingAmount = int(amount * 100)

# Find the number of one dollars
numberOfOneDollars = remainingAmount // 100
remainingAmount = remainingAmount % 100

# Find the number of quarters in the remaining amount
numberOfQuarters = remainingAmount // 25
remainingAmount = remainingAmount % 25

# Find the number of dimes in the remaining amount
numberOfDimes = remainingAmount // 10
remainingAmount = remainingAmount % 10

# Find the number of nickels in the remaining amount
numberOfNickels = remainingAmount // 5
remainingAmount = remainingAmount % 5

# Find the number of pennies in the remaining amount
numberOfPennies = remainingAmount

# Display results
print("Your amount", amount, "consists of")
if numberOfOneDollars > 0:
    print(" " + str(numberOfOneDollars), "dollars" if numberOfOneDollars > 1 else "dollar")
if numberOfQuarters > 0:
    print(" " + str(numberOfQuarters), "quarters" if numberOfQuarters > 1 else "quarter")
if numberOfDimes > 0:
    print(" " + str(numberOfDimes), "dimes" if numberOfDimes > 1 else "dime")
if numberOfNickels > 0:
    print(" " + str(numberOfNickels), "nickels" if numberOfNickels > 1 else "nickel")
if numberOfPennies > 0:
    print(" " + str(numberOfPennies), "pennies" if numberOfPennies > 1 else "penny")
