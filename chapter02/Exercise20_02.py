'''*2.20 (Financial application: calculate interest) If you know the balance and the annual
          percentage interest rate, you can compute the interest on the next monthly payment
          using the following formula:
                   interest = balance * (annualInterestRate / 1200)
          Write a program that reads the balance and the annual percentage interest rate
          and displays the interest for the next month.


/**
 * @author BASSAM FARAMAWI
 * @email tiodaronzi3@yahoo.com
 * @since 2018
 */
'''
# Enter the balance and the annual percentage interest rate
balance, annualInterestRate = eval(input("Enter balance and interest rate (e.g., 3 for 3%): "))

# Compute the interest on the next monthly payment
interest = balance * (annualInterestRate / 1200)

# Display the result
print("The interest is ", int(interest * 100000) / 100000)
