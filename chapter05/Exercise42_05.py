'''
**5.42 (Monte Carlo simulation) A square is divided into four smaller regions as shown in
(a). If you throw a dart into the square one million times, what is the probability for
the dart to fall into an odd-numbered region? Write a program to simulate the
process and display the result. (Hint: Place the center of the square in the center of
a coordinate system, as shown in (b). Randomly generate a point in the square and
count the number of times for a point to fall in an odd-numbered region.)

/**
 * @author BASSAM FARAMAWI
 * @email tiodaronzi3@yahoo.com
 * @since 2018
 */
'''
from random import randint

SQUARE_SIDE = 10  # The square side as a constant
COUNT = 1000000

oddRegion = 0
evenRegion = 0

# Points of line between region 2 and 3
x0, y0, x1, y1 = 5, 0, 0, 5

for i in range(COUNT) :
    # Randomly generate the point coordinates
    x = randint(-5, 5)
    y = randint(-5, 5)

    if x == 0 or y == 0 :  # Will not count points that is on x or y axis
        continue

    elif x < 0 : # If point in region 1
        oddRegion += 1

    elif y < 0 :  # If point in region 4
        evenRegion += 1

    elif y > 0 :  # If in region 2 or 3
        if(x1 - x0)*(y - y0) - (x - x0)*(y1 - y0) == 0 :
            continue # Neglect the points on the line between region 2 and 3

        elif(x1 - x0)*(y - y0) - (x - x0)*(y1 - y0) > 0 :
            oddRegion += 1  # On the left side of the line (region 3)

        elif(x1 - x0)*(y - y0) - (x - x0)*(y1 - y0) < 0 :
            evenRegion += 1  # On the right side of the line (region 2)

oddProbability = oddRegion / float(COUNT)
evenProbability = evenRegion / float(COUNT)

# Display the result
print("oddProbability = %" + str(oddProbability))
print("evenProbability = %" + str(evenProbability))