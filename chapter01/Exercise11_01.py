'''
*1.11 (Population projection) The US Census Bureau projects population based on the
      following assumptions:
      One birth every 7 seconds
      One death every 13 seconds
      One new immigrant every 45 seconds
      Write a program to display the population for each of the next five years. Assume the
      current population is 312032486 and one year has 365 days. Hint: in Python, you
      can use integer division operator // to perform division. The result is an integer. For
      example, 5 // 4 is 1 (not 1.25) and 10 // 4 is 2 (not 2.5).

/**
 * @author BASSAM FARAMAWI
 * @since 2018
 */
'''

# Calculate and display the population for each year
print("The population for:")
print("  Year one = ", 312032486 + 365 * 24 * 3600 // 7 + 365 * 24 * 3600 // 45 - 365 * 24 * 3600 // 13)
print("  Year tow = ", 312032486 + 2 * 365 * 24 * 3600 // 7 + 365 * 24 * 3600 // 45 - 365 * 24 * 3600 // 13)
print("  Year three = ", 312032486 + 3 * 365 * 24 * 3600 // 7 + 365 * 24 * 3600 // 45 - 365 * 24 * 3600 // 13)
print("  Year four = ", 312032486 + 4 * 365 * 24 * 3600 // 7 + 365 * 24 * 3600 // 45 - 365 * 24 * 3600 // 13)
print("  Year five = ", 312032486 + 5 * 365 * 24 * 3600 // 7 + 365 * 24 * 3600 // 45 - 365 * 24 * 3600 // 13)
