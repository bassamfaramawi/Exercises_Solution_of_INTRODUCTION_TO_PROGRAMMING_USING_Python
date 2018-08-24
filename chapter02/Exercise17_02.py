''' *2.17 (Health application: compute BMI) Body mass index (BMI) is a measure of health
           based on weight. It can be calculated by taking your weight in kilograms and
           dividing it by the square of your height in meters. Write a program that prompts
           the user to enter a weight in pounds and height in inches and displays the BMI.
           Note that one pound is 0.45359237 kilograms and one inch is 0.0254 meters.


/**
 * @author BASSAM FARAMAWI
 * @email tiodaronzi3@yahoo.com
 * @since 2018
 */
'''
# Prompt the user for inputting the weight in pounds and the height in inches
weight = eval(input("Enter weight in pounds: "))
height = eval(input("Enter height in inches: "))

# Convert to kilograms and meters
weight *= 0.54359237
height *= 0.0254

# Compute BMI
BMI = weight / (height ** 2)

# Display the result
print("BMI is", int(BMI * 10000) / 10000)
