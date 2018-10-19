'''
*5.33 (Financial application: compute CD value) Suppose you put $10,000 into a
CD with an annual percentage yield of 5.75%. After one month, the CD is worth
10000 + 10000 * 5.75 / 1200 = 10047.92
After two months, the CD is worth
10047.91 + 10047.91 * 5.75 / 1200 = 10096.06
After three months, the CD is worth
10096.06 + 10096.06 * 5.75 / 1200 = 10144.44
and so on.
Write a program that prompts the user to enter an amount (e.g., 10000), the
annual percentage yield (e.g., 5.75), and the number of months (e.g., 18) and
displays a table as shown in the sample run.

/**
 * @author BASSAM FARAMAWI
 * @email tiodaronzi3@yahoo.com
 * @since 2018
 */
'''
#Prompt the user to enter the initial deposit amount
amount = eval(input("Enter the initial deposit amount: "))

#Prompt the user to enter the annual percentage yield
annualPercentageYield = eval(input("Enter annual percentage yield: "))

#Prompt the user to enter the number of months
numberOfMonths = eval(input("Enter maturity period (number of months): "))

CDValue = amount  # Initialize monthly amount

# Print the header
print("\n" + format("Month", "<8s") + format("CD Value", "<8s"))

# Print the table body
for n in range(1, numberOfMonths + 1):
    CDValue *= (1 + annualPercentageYield / 1200)
    print(format(n, "<8d") , format(CDValue, "<8.2f"))