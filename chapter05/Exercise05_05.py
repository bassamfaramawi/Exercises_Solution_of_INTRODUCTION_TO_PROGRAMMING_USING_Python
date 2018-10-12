'''
 5.5 (Conversion from kilograms to pounds and pounds to kilograms) Write a program
      that displays the following two tables side by side:
        Kilograms    Pounds     |     Pounds     Kilograms
        1            2.2        |     20         9.09
        3            2.2        |     25         11.36
        ...
        197          433.4      |     510        231.82
        199          437.8      |     515        234.09

/**
 * @author BASSAM FARAMAWI
 * @email tiodaronzi3@yahoo.com
 * @since 2018
 */
'''
POUNDS_PER_KILOGRAMS = 2.2;  # POUNDS_PER_KILOGRAMS

# Print the header
print(format("Kilograms", "<12s"), format("Pounds", "<10s"),
      format("|", "<9s"), format("Pounds", "<10s"),
      format("Kilograms", "<12s"))

pounds = 20  # Initialize pounds

# Loop for the table body
for kilograms in range(1, 200):
    print(format(kilograms, "<12d"),
          format(kilograms * POUNDS_PER_KILOGRAMS, "<10.1f"),
          format("|", "<9s"), format(pounds, "<10d"),
          format(pounds / POUNDS_PER_KILOGRAMS, "<12.2f"))
    pounds += 5
