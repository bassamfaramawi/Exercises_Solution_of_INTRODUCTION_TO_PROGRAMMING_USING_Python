'''*3.3 (Geography: estimate areas) Find the GPS locations for Atlanta, Georgia;
         Orlando, Florida; Savannah, Georgia; and Charlotte, North Carolina from
         www.gps-data-team.com/map/ and compute the estimated area enclosed by these
         four cities. (Hint: Use the formula in Programming Exercise 3.2 to compute the
         distance between two cities. Divide the polygon into two triangles and use the formula
         in Programming Exercise 2.14 to compute the area of a triangle.)


/**
 * @author BASSAM FARAMAWI
 * @email tiodaronzi3@yahoo.com
 * @since 2018
 */
'''
import math  # Import cmath module

EARTH_RADIUS = 6371.01  # earth radius in Km as a constant

# Atlanta, Georgia coordinates (latitude, longitude)
x1 = math.radians(33.7489954)
y1 = math.radians(-84.3879824)

# Orlando, Florida coordinates (latitude, longitude)
x2 = math.radians(28.5383355)
y2 = math.radians(-81.37923649999999)

# Savannah, Georgia coordinates (latitude, longitude)
x3 = math.radians(32.0808989)
y3 = math.radians(-81.09120300000001)

# Charlotte, North Carolina coordinates (latitude, longitude)
x4 = math.radians(35.2270869)
y4 = math.radians(-80.84312669999997)

# Compute the three sides of the first triangle of the polygon (Atlanta - Orlando - Savannah)
side1 = EARTH_RADIUS * math.acos(math.sin(x1) * math.sin(x2) + math.cos(x1) * math.cos(x2) * math.cos(y1 - y2))
side2 = EARTH_RADIUS * math.acos(math.sin(x2) * math.sin(x3) + math.cos(x2) * math.cos(x3) * math.cos(y2 - y3))
# The side between the 2 triangles
side3 = EARTH_RADIUS * math.acos(math.sin(x3) * math.sin(x1) + math.cos(x3) * math.cos(x1) * math.cos(y3 - y1))

# Compute s2
s1 = (side1 + side2 + side3) / 2

# Compute the area
area1 = (2 * s1 * (s1 - side1) * (s1 - side2) * (s1 - side3)) ** 0.5

# compute the tow left sides of the second triangle of the polygon (Atlanta - Charlotte - Savannah)
side4 = EARTH_RADIUS * math.acos(math.sin(x1) * math.sin(x4) + math.cos(x1) * math.cos(x4) * math.cos(y1 - y4))
side5 = EARTH_RADIUS * math.acos(math.sin(x4) * math.sin(x3) + math.cos(x4) * math.cos(x3) * math.cos(y4 - y3))

# Compute s2
s2 = (side4 + side5 + side3) / 2

# Compute the area
area2 = (2 * s2 * (s2 - side4) * (s2 - side5) * (s2 - side3)) ** 0.5

area = area1 + area2  # the polygon hole area

# Display the result
print("The estimated area enclosed by these four cities(Atlanta - Orlando - Savannah - Charlotte) is:", area, "Km2")
