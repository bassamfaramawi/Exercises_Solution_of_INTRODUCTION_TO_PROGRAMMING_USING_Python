'''


/**
 * @author BASSAM FARAMAWI
 * @email tiodaronzi3@yahoo.com
 * @since 2018
 */
'''
# Receive the amount
amount = eval(input("Enter an amount in cents, for example, 1156: "))

# Find the number of one dollars
numberOfOneDollars = amount // 100

remainingAmount = amount % 100

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

# Display the results
print("Your amount", amount, "consists of\n",
      "\t", numberOfOneDollars, "dollars\n",
      "\t", numberOfQuarters, "quarters\n",
      "\t", numberOfDimes, "dimes\n",
      "\t", numberOfNickels, "nickels\n",
      "\t", numberOfPennies, "pennies")
