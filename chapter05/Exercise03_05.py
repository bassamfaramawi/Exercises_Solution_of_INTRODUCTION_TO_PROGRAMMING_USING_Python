'''
5.3 (Conversion from kilograms to pounds) Write a program that displays the following
table (note that 1 kilogram is 2.2 pounds):
        Kilograms     Pounds
        1               2.2
        3               6.6
        ...
        197           433.4
        199           437.8

/**
 * @author BASSAM FARAMAWI
 * @email tiodaronzi3@yahoo.com
 * @since 2018
 */
'''
POUNDS_PER_KILOGRAMS = 2.2;  # POUNDS_PER_KILOGRAMS

# Print the header
print(format("Kilograms", "<18s"),
      format("Pounds", "<14s"))

# Loop for the table body
for n in range(1, 200, 2):
    print(format(n, "<18d"),
          format(n * POUNDS_PER_KILOGRAMS, "<14.1f"))
