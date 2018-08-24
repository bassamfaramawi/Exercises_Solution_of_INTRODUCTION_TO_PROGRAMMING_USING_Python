''' 2.15 (Geometry: area of a hexagon) Write a program that prompts the user to enter the
          side of a hexagon and displays its area. The formula for computing the area of a
          hexagon is Area = 3 * 3 ** 0.5 / 2 * s ** 2 where s is the length of a side.


/**
 * @author BASSAM FARAMAWI
 * @email tiodaronzi3@yahoo.com
 * @since 2018
 */
'''
# Prompet the user for inputting the side
side = eval(input("Enter the side: "))

# Compute the area
Area = 3 * 3 ** 0.5 / 2 * side ** 2

# Display the result
print("The area of the hexagon is ", int(Area * 10000) / 10000)
