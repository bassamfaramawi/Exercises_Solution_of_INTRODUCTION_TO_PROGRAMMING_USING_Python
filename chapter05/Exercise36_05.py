'''
***5.36 (Game: scissor, rock, paper) Programming Exercise 4.17 gives a program that
plays the scissor, rock, paper game. Revise the program to let the user play continuously
until either the user or the computer wins more than two times.

/**
 * @author BASSAM FARAMAWI
 * @email tiodaronzi3@yahoo.com
 * @since 2018
 */
'''
import random

computerWinings = 0
userWinings = 0

print("The target score is 2, lets start the game\n")

while abs(computerWinings - userWinings) < 2:
    computerChoise =  random.randint(0, 2)

    #Prompt the user to enter to enter a number 0, 1, or 2
    userChoise = eval(input("\nscissor (0), rock (1), paper (2): "))

    # Initialize guess and computer names
    guessName =""
    computerName = " "

    # Assign computer names
    computerName = "scissor" if computerChoise == 0 else "rock" \
        if computerChoise == 1 else "paper"

    # Assign user guess names
    guessName = "scissor" if userChoise == 0 else "rock" \
        if userChoise == 1 else "paper"

    # Check won or draw or lose and display the result
    if userChoise == computerChoise:
        print("The computer is", computerName + ". You are"
                , guessName, "too. It is a draw")
    elif(computerChoise == 0 and userChoise == 2) or\
            (computerChoise == 1 and userChoise == 0) or\
            (computerChoise == 2 and userChoise == 1) :
        print("The computer is", computerName + ". You are"
                , guessName + ". You lose")
        computerWinings += 1

    elif(computerChoise == 2 and userChoise == 0) or\
            (computerChoise == 0 and userChoise == 1) or\
            (computerChoise == 1 and userChoise == 2) :
        print("The computer is", computerName + ". You are"
                , guessName + ". You won")
        userWinings += 1

# Print the winner
print("\n" + "You are" if userWinings > computerWinings else
        " The computer is", "the winner.")