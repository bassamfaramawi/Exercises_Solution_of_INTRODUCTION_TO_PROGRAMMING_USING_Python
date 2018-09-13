'''
*3.9 (Financial application: payroll) Write a program that reads the following information
      and prints a payroll statement:
         Employee’s name (e.g., Smith)
         Number of hours worked in a week (e.g., 10)
         Hourly pay rate (e.g., 9.75)
         Federal tax withholding rate (e.g., 20%)
         State tax withholding rate (e.g., 9%)


/**
 * @author BASSAM FARAMAWI
 * @email tiodaronzi3@yahoo.com
 * @since 2018
 */
'''

# Prompt the user to enter Employee’s name,
name = input("Enter employee's name:")

# Number of hours worked in a week,
weeklyHours = eval(input("Number of hours worked in a week:"))

#  Hourly pay rate,
hourlyPayRate = eval(input("Hourly pay rate:"))

# Federal tax withholding rate,
federalTax = eval(input("Federal tax withholding rate:"))

# And State tax withholding rate
stateTax = eval(input("State tax withholding rate:"))

# Calculate Gross Pay,
grossPay = weeklyHours * hourlyPayRate

# Federal Withholding,
federalWithholding = grossPay * federalTax

# State Withholding,
stateWithholding = grossPay * stateTax

# Total Deduction,
totalDeduction = federalWithholding + stateWithholding

# And Net Pay
netPay = grossPay - totalDeduction

# Display the results
print("\nEmployee Name: " + name +
      "\nPay Rate: $" + str(hourlyPayRate) +
      "\nGross Pay: $" + str(grossPay) +
      "\nDeductions:" +
      "\n  Federal Withholding (20.0%): $" + str(federalWithholding) +
      "\n  State Withholding (9.0%): $" + str(stateWithholding) +
      "\n  Total Deduction: $" + str(totalDeduction) +
      "\nNet Pay: $" + str(netPay))
