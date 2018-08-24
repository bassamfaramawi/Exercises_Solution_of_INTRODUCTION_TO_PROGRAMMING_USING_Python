'''*2.11 (Financial application: investment amount) Suppose you want to deposit a
          certain amount of money into a savings account with a fixed annual interest rate.
          What amount do you need to deposit in order to have $5,000 in the account after
          three years? The initial deposit amount can be obtained using the following formula:

               initialDepositAmount = finalAccountValue /( (1 + monthlyInterestRate) ** numberOfMonths)

       Write a program that prompts the user to enter final account value, annual interest
       rate in percent, and the number of years, and displays the initial deposit amount.


/**
 * @author BASSAM FARAMAWI
 * @email tiodaronzi3@yahoo.com
 * @since 2018
 */
'''
# Prompt the user for inputting final account value
finalAccountValue = eval(input("Enter the final account value: "))

# Prompt the user for inputting annual interest rate in percent
annualInterestRate = eval(input("Enter annual interest rate in percent: "))

# Prompt the user for inputting the number of years
numberOfYears = eval(input("Enter number of years: "))

# Compute the number of months
numberOfMonths = numberOfYears * 12

# Compute the monthly interest rate
monthlyInterestRate = annualInterestRate / 1200

# Compute the initial deposit amount
initialDepositAmount = finalAccountValue / (1 + monthlyInterestRate) ** numberOfMonths

# Display the result
print("Initial deposit value is", initialDepositAmount)
