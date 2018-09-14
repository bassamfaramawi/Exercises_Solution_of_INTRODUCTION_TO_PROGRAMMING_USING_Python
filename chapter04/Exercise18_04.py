'''
*4.18 (Financials: currency exchange) Write a program that prompts the user to enter
the currency exchange rate between U.S. dollars and Chinese Renminbi (RMB).
Prompt the user to enter 0 to convert from U.S. dollars to Chinese RMB and 1 for
vice versa. Prompt the user to enter the amount in U.S. dollars or Chinese RMB to
convert it to Chinese RMB or U.S. dollars, respectively.

/**
 * @author BASSAM FARAMAWI
 * @email tiodaronzi3@yahoo.com
 * @since 2018
 */
'''
# Asking to enter exchange rate from dollar to RMB
exchangeRate = eval(input("Enter the exchange rate from dollars to RMB: "))

# Asking to enter 0 to convert dollars to RMB and 1 vice versa
convert = eval(input("Enter 0 to convert dollars to RMB and 1 vice versa: "))

# Initialize dollars double and RMB double double dollars, RMB
if convert == 0:  # If 0 convert from dollars to RMB case
    # Asking to enter the dollar amount
    dollars = eval(input("Enter the dollar amount: "))
    # Calculate RMB and display the result
    RMB = dollars * exchangeRate
    print("$" + str(dollars) + " is " + format(RMB, ".2f") + " yuan")
elif convert == 1:  # If 1 convert from RMB to dollars case
    # Asking to enter the RMB amount
    RMB = eval(input("Enter the RMB amount: "))
    # Calculate dollars and display the result
    dollars = RMB / exchangeRate
    print(str(RMB) + "yuan is $" + format(dollars, ".2f")) \
        # Otherwise is an incorrect input
else:
    print("Incorrect input")
