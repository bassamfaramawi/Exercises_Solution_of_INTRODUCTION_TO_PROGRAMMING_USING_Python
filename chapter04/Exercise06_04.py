'''
*4.6 (Health application: BMI ) Revise Listing 4.6, ComputeBMI.py, to let users enter
their weight in pounds and their height in feet and inches. For example, if a person
is 5 feet and 10 inches, you will enter 5 for feet and 10 for inches.
/**
 * @author BASSAM FARAMAWI
 * @email tiodaronzi3@yahoo.com
 * @since 2018
 */
'''
# Prompt the user to enter weight in pounds
weight = eval(input("Enter weight in pounds: "))

# Prompt the user to enter feet
feet = eval(input("Enter feet: "))

# Prompt the user to enter inches
inches = eval(input("Enter inches: "))

KILOGRAMS_PER_POUND = 0.45359237;  # Kilograms per pound
METERS_PER_INCH = 0.0254;  # Meters per inch
FEET_PER_METER = 3.280839895;  # Feet per meter

# Convert pounds to kilograms
kilogrames = weight * KILOGRAMS_PER_POUND
# Convert (Feet + inches) to meters
meters = feet / FEET_PER_METER + inches * METERS_PER_INCH
# Calculate BMI
BMI = kilogrames / (meters * meters);

# Display the result
print("BMI is", BMI);

if (BMI < 18.5):
    print("Underweight")
elif (BMI < 25):
    print("Normal")
elif (BMI < 30):
    print("Overweight")
else:
    print("Obese")
