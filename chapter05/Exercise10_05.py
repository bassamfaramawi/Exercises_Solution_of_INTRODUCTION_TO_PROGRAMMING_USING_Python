'''
5.10 (Find the highest score) Write a program that prompts the user to
enter the number of students and each student’s score, and displays the
highest score. Assume that the input is stored in a file named score.txt,
and the program obtains the input from the file.

/**
 * @author BASSAM FARAMAWI
 * @email tiodaronzi3@yahoo.com
 * @since 2018
 */
'''
# Prompt the user to enter the number of students
studentsNumber = eval(input("Enter the number of students: "))

# Initialize name and the score of the highest score student
highestName = ""
highestScore = 0

# Loop for students scores
for n in range(1, studentsNumber + 1):
    studentName = input("Enter the name of student no." +
                        str(n) + ": ")
    studentScore = eval(input("Enter the student score: "))
    # Determine the highest score student
    if studentScore > highestScore:
        highestName = studentName;
        highestScore = studentScore;

# Display the result
print("The student with the highest score is", highestName
      , "with score =", highestScore)
