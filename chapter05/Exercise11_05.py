'''
*5.11 (Find the two highest scores) Write a program that prompts the user
to enter the number of students and each student’s score, and displays the
highest and secondhighest scores.

/**
 * @author BASSAM FARAMAWI
 * @email tiodaronzi3@yahoo.com
 * @since 2018
 */
'''
# Prompt the user to enter the number of students
studentsNumber = eval(input("Enter the number of students: "))

# Initialize the name of the 1'st and 2'nd score students
highestName = ""
secondHighestName = ""
# Initialize the 1'st and 2'nd scores
highestScore = 0
secondHighestScore = 0

# Loop for students scores
for n in range(1, studentsNumber + 1):
    studentName = input("Enter the name of student no." + str(n) + ": ")
    studentScore = eval(input("Enter the student score: "))
    # Determine the 1st and 2nd highest score student
    if studentScore > highestScore and studentScore > secondHighestScore:
        secondHighestName = highestName
        secondHighestScore = highestScore
        highestName = studentName;
        highestScore = studentScore;

    elif studentScore > secondHighestScore:
        secondHighestName = studentName
        secondHighestScore = studentScore

# Display the result
print("The student with the highest score is", highestName,
      "with score =", highestScore)

print("The student with the second highest score is",
      secondHighestName, "with score =", secondHighestScore)
