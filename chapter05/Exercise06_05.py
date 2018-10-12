'''
5.6 (Conversion from miles to kilometers) Write a program that displays the following
two tables side by side:
            Miles      Kilometers    |      Kilometers       Miles
            1          1.609         |      20               12.430
            2          3.218         |      25               15.538
            ...
            9          14.481        |      60               37.290
            10         16.090        |      65               40.398

/**
 * @author BASSAM FARAMAWI
 * @email tiodaronzi3@yahoo.com
 * @since 2018
 */
'''
KILOMETERS_PER_MILES = 1.609;  # KILOMETERS_PER_MILES

# Print the header
print(format("Miles", "<12s"),
      format("Kilometers", "<12s"),
      format("|", "<9s"),
      format("Kilometers", "<12s"),
      format("Miles", "<12s"))

kilometers = 20  # Initialize miles

# Loop for the table body
for miles in range(1, 10 + 1):
    print(format(miles, "<12d"),
          format(miles * KILOMETERS_PER_MILES, "<12.3f"),
          format("|", "<9s"), format(kilometers, "<12d"),
          format(kilometers / KILOMETERS_PER_MILES, "<12.3f"))
    kilometers += 5
