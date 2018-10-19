'''
 *5.39 (Financial application: find the sales amount) You have just started a
sales job in a department store. Your pay consists of a base salary and a
commission. The base salary is $5,000. The scheme shown below is used to
determine the commission rate.

       Sales Amount                Commission Rate
       $0.01–$5,000                8 percent
       $5,000.01–$10,000           10 percent
       $10,000.01 and above        12 percent

Note that this is a graduated rate. The rate for the first $5,000 is at 8%, the
next $5000 is at 10%, and the rest is at 12%. If the sales amount is 25,000, the
commission is 5,000 * 8% + 5,000 * 10% + 15,000 * 12% = 2,700.
Your goal is to earn $30,000 a year. Write a program that finds the minimum
sales you have to generate in order to make $30,000.

/**
 * @author BASSAM FARAMAWI
 * @email tiodaronzi3@yahoo.com
 * @since 2018
 */
'''
# The commission target in a year
commissionPerYear = 30000
# Get the monthly commission target
commissionPerMonth = commissionPerYear / 12

salesAmount = 0.01  # Initialize the sales amount
commission = 0  # Initialize the commission needed

while commission < commissionPerMonth :
    salesAmount += 0.01
    if salesAmount > 10000.01 :
        commission = (salesAmount - 10000) * 0.12 + 5000 * 0.10 + \
                5000 * 0.08
    elif salesAmount > 5000.01 :
        commission = (salesAmount - 5000) * 0.10 + 5000 * 0.08
    else :
        commission = salesAmount * 0.08

# Display the result
print("You need $" + format(salesAmount, "<.2f"),
      "monthly sales amount to make a commission of $30000 per year")