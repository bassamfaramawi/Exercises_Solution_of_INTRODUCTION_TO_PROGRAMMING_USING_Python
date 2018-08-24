'''*2.19 (Financial application: calculate future investment value) Write a program that
         reads in an investment amount, the annual interest rate, and the number of years,
         and displays the future investment value using the following formula:
                      futureInvestmentValue = investmentAmount * (1 + monthlyInterestRate)**numberOfMonths
         For example, if you enter the amount 1000, an annual interest rate of 4.25%,
        and the number of years as 1, the future investment value is 1043.33.

/**
 * @author BASSAM FARAMAWI
 * @email tiodaronzi3@yahoo.com
 * @since 2018
 */
'''
investmentAmount = eval(input("Enter investment amount: "))  # Enter investment amount

annualInterestRate = eval(input("Enter annual interest rate: "))  # Enter annual interest rate

monthlyInterestRate = annualInterestRate / 1200  # Calculate the monthly interest rate

numberOfYears = eval(input("Enter number of years: "))  # Enter number of years

numberOfMonths = 12 * numberOfYears  # Calculate number of months

# Calculate future investment value
futureInvestmentValue = investmentAmount * (1 + monthlyInterestRate) ** numberOfMonths

# Display results
print("Accumulated value is ", int(futureInvestmentValue * 100) / 100)
