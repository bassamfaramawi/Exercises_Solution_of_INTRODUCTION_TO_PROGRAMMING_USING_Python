'''
 2.2 (Compute the volume of a cylinder) Write a program that reads in the radius
      and length of a cylinder and computes the area and volume using the following
      formulas:
      area = radius * radius * p
      volume = area * length

/**
 * @author BASSAM FARAMAWI
 * @email tiodaronzi3@yahoo.com
 * @since 2018
 */
'''
PI = 3.14259
# Prompt the user for inputting the radius and length
radius, length = eval(input("Enter the radius and length of a cylinder: "))

# Compute the area
area = radius ** 2 * PI

# Compute the volume
volume = area * length

# Display results
print("The area is", int(area * 10000) / 10000)
print("The volume is", int(volume * 100) / 100)
