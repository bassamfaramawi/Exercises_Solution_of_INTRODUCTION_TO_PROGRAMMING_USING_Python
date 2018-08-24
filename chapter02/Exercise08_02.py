'''
 2.8 (Science: calculating energy) Write a program that calculates the energy
      needed to heat water from an initial temperature to a final temperature. Your
      program should prompt the user to enter the amount of water in kilograms and the
      initial and final temperatures of the water. The formula to compute the energy is
      Q = M * (finalTemperature – initialTemperature) * 4184
      where M is the weight of water in kilograms, temperatures are in degrees Celsius,
      and energy Q is measured in joules

/**
 * @author BASSAM FARAMAWI
 * @email tiodaronzi3@yahoo.com
 * @since 2018
 */
'''

# Prompet the user for inputting the amountt of water in kilograms
kilograms = eval(input("Enter the amount of water in kilograms: "))

# Prompet the user for inputting the initial temperature
initialTemperature = eval(input("Enter the initial temperature: "))

# Prompet the user for inputting the final temperature
finalTemperature = eval(input("Enter the final temperature: "))

# Compute the energy
energy = kilograms * (finalTemperature - initialTemperature) * 4184

# Display the results
print("The energy needed is", energy)
