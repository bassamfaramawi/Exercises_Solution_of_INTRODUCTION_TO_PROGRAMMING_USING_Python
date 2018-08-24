'''**2.21 (Financial application: compound value) Suppose you save $100 each month into
           a savings account with an annual interest rate of 5%. Therefore, the monthly interest
           rate is After the first month, the value in the account
           becomes
                       100 * (1 + 0.00417) = 100.417
           After the second month, the value in the account becomes
                      (100 + 100.417) * (1 + 0.00417) = 201.252
           After the third month, the value in the account becomes
                      (100 + 201.252) * (1 + 0.00417) = 302.507
           and so on.
    Write a program that prompts the user to enter a monthly saving amount and
    displays the account value after the sixth month.


/**
 * @author BASSAM FARAMAWI
 * @email tiodaronzi3@yahoo.com
 * @since 2018
 */
'''
# prompts the user to enter a monthly saving amount
monthlyAmount = eval(input("Enter the monthly saving amount: "))

# Compute the monthly factor
annualInterestRate = 0.05
monthlyInterestRate = annualInterestRate / 12
monthlyFactor = 1 + monthlyInterestRate

# Compute the value after six months
firstValue = monthlyAmount * monthlyFactor
secondValue = (monthlyAmount + firstValue) * monthlyFactor
thirdValue = (monthlyAmount + secondValue) * monthlyFactor
forthValue = (monthlyAmount + thirdValue) * monthlyFactor
fifthValue = (monthlyAmount + forthValue) * monthlyFactor
sixValue = (monthlyAmount + fifthValue) * monthlyFactor

# Display the result
print("After the sixth month, the account value is ", int(sixValue * 100) / 100)
