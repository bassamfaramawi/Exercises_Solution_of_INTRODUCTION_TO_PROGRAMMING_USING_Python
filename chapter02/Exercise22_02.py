'''2.22 (Population projection) Rewrite Exercise 1.11 to prompt the user to enter the
         number of years and displays the population after that many years.

/**
 * @author BASSAM FARAMAWI
 * @email tiodaronzi3@yahoo.com
 * @since 2018
 */
'''

numberOfYears = eval(input("Enter the number of years: "))  # Enter the number of years

currentPopulation = 312032486

totalSeconds = numberOfYears * 365 * 24 * 3600  # Compute the toltal seconds in the years

# Compute the final population
finalPopulation = currentPopulation + totalSeconds // 7 + totalSeconds // 45 - totalSeconds // 13

# Display the result
print("The population in", numberOfYears, "years is", finalPopulation)
