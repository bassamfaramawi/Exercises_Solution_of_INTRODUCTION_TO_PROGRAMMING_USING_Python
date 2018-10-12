'''
5.4 (Conversion from miles to kilometers) Write a program that displays the following
table (note that 1 mile is 1.609 kilometers):
        Miles     Kilometers
        1         1.609
        2         3.218
        ...
        9         14.481
        10        16.090

/**
 * @author BASSAM FARAMAWI
 * @email tiodaronzi3@yahoo.com
 * @since 2018
 */
'''
KILOMETERS_PER_MILES = 1.609;  # KILOMETERS_PER_MILES

# Print the header
print(format("Miles", "<14s"),
      format("Kilometers", "<18s"))

# Loop for the table body
for n in range(1, 11):
    print(format(n, "<14d"),
          format(n * KILOMETERS_PER_MILES, "<18.3f"))
