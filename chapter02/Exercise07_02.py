'''
 2.7 (Find the number of years) Write a program that prompts the user to
      enter the minutes (e.g., 1 billion), and displays the number of years and
      days for the minutes. For simplicity, assume a year has 365 days

/**
 * @author BASSAM FARAMAWI
 * @email tiodaronzi3@yahoo.com
 * @since 2018
 */
'''

# Prompet hte user for inputting minutes
minutes = eval(input("Enter the number of minutes: "))

# Compute the number of years and days
years = minutes // (60 * 24 * 365)
days = minutes % (60 * 24 * 365) // (60 * 24)

# Display results
print(minutes, "minutes is approximately", years, "years and", days, "days")
