'''
5.7 (Use trigonometric functions) Print the following table to
display the sin value and cos value of degrees from 0 to 360
with increments of 10 degrees. Round the value to keep four
digits after the decimal point.

   Degree    Sin         Cos
   0         0.0000      1.0000
   10        0.1736      0.9848
   ...
   350       -0.1736     0.9848
   360       0.0000      1.0000

/**
 * @author BASSAM FARAMAWI
 * @email tiodaronzi3@yahoo.com
 * @since 2018
 */
'''
import math

# Print the header
print(format("Degree", "<12s"), format("Sin", "<12s"),
      format("Cos", "<12s"))

# Print the table body
for degree in range(0, 360 + 10, 10):
    print(format(degree, "<12d"),
          format(math.sin(degree * math.pi / 180), "<12.4f"),
          format(math.cos(degree * math.pi / 180), "<12.4f"))
