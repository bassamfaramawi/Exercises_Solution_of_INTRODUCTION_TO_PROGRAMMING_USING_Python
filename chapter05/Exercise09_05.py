'''
**5.9 (Financial application: compute future tuition) Suppose that
the tuition for a university is $10,000 this year and increases 5%
every year. Write a program that computes the tuition in ten years
and the total cost of four years’ worth of tuition starting ten
years from now.

/**
 * @author BASSAM FARAMAWI
 * @email tiodaronzi3@yahoo.com
 * @since 2018
 */
'''
NUMBER_OF_YEARS = 14;  # 10 Years + 4 years after it
tuition = 10000;  # initialize tuition
increaseRate = 0.05;  # Every year increment

for n in range(1, NUMBER_OF_YEARS + 1):
    tuition *= (1 + increaseRate)
    if n == 10:  # Display the tuition after 10 years
        print("The tuition after ten years is $" +
              format(tuition, "<.2f"))

# Display the total cost of 4 years after the tenth year
print("Total cost of 4 years after the tenth year: $" +
      format(tuition, "<.2f"));
