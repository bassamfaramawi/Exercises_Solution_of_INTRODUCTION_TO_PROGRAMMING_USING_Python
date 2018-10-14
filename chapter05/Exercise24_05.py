'''
**5.24 (Financial application: loan amortization schedule)
The monthly payment for a given loan pays the principal and
the interest. The monthly interest is computed by multiplying
the monthly interest rate and the balance (the remaining principal).
The principal paid for the month is therefore the monthly payment
minus the monthly interest. Write a program that lets the user enter
the loan amount, number of years, and interest rate, and then displays
the amortization schedule for the loan.

/**
 * @author BASSAM FARAMAWI
 * @email tiodaronzi3@yahoo.com
 * @since 2018
 */
'''
# Let the user enter loan amount
loanAmount = eval(input("Loan Amount: "))
# Let the user enter loan amount
numberOfYears = eval(input("Number of Years: "))
# Let the user enter annual interest rate
annualInterestRate = eval(input("Annual Interest Rate: "))

# The monthly interest rate
monthlyInterestRate = annualInterestRate / 1200
# The monthly payment
monthlyPayment = loanAmount * monthlyInterestRate / (1 - 1 / \
                                                     pow(1 + monthlyInterestRate, numberOfYears * 12))
# The total payment
totalPayment = monthlyPayment * numberOfYears * 12

# Display the monthly payment and the total payment
print()
print("Monthly Payment: %" + format(monthlyPayment, "<.2f"))
print("Total Payment: %" + format(totalPayment, "<.2f"))
print()

balance = loanAmount

# Print the header
print(format("Payment#", "<15s"), format("Interest", "<15s"),
      format("Principal", "<15s"), format("Balance", "<15s"))

# Loop for printing the table body
for n in range(1, numberOfYears * 12 + 1):
    interest = monthlyInterestRate * balance
    principal = monthlyPayment - interest
    balance = balance - principal

    # Display the results
    print(format(n, "<15d"),
          format(interest, "<15.2f"),
          format(principal, "<15.2f"),
          format(balance, "<15.2f"))
