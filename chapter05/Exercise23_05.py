'''
**5.23 (Financial application: compare loans with various
interest rates) Write a program that lets the user enter
the loan amount and loan period in number of years and
displays the monthly and total payments for each interest
rate starting from 5% to 8%, with an increment of 1/8.

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
interestRate = 5.0 # Initialize interest rate from 5 %
increment = 0.125  # The increment

count = int((8 - 5) / 0.125) # The loop count number

# Print the header
print(format("Interest Rate", "<17s"),
      format("Monthly Payment", "<17s"),
      format("Total Payment", "<17s"))

for n in range(count + 1):  # Loop for printing the table body
    annualInterestRate = n * increment + interestRate
    monthlyInterestRate = annualInterestRate / 1200
    monthlyPayment = loanAmount * monthlyInterestRate / \
                     (1 - 1 / pow(1 + monthlyInterestRate, numberOfYears * 12))
    totalPayment = monthlyPayment * numberOfYears * 12

    # Display the result
    print(format(annualInterestRate, "<17.3f"),
          format(monthlyPayment, "<17.2f"),
          format(totalPayment, "<17.2f"))