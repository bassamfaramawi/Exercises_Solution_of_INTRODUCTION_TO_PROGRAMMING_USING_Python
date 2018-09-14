'''
*4.17 (Game: scissor, rock, paper) Write a program that plays the popular scissor-rockpaper
game. (A scissor can cut a paper, a rock can knock a scissor, and a paper can
wrap a rock.) The program randomly generates a number 0, 1, or 2 representing
scissor, rock, and paper. The program prompts the user to enter a number 0, 1, or
2 and displays a message indicating whether the user or the computer wins, loses,
or draws.

/**
 * @author BASSAM FARAMAWI
 * @email tiodaronzi3@yahoo.com
 * @since 2018
 */
'''
import random

computer = random.randrange(0, 3)

# Prompt the user to enter to enter a number 0, 1, or 2
guess = eval(input("scissor (0), rock (1), paper (2): "))

if computer == 0:
    computerName = "scissor"
elif computer == 1:
    computerName = "rock"
elif computer == 2:
    computerName = "paper"

if guess == 0:
    guessName = "scissor"
elif guess == 1:
    guessName = "rock"
elif guess == 2:
    guessName = "paper"

# Check won or draw or lose and display the result
if (guess == computer):
    print("The computer is", computerName, ". You are", guessName, "too. It is a draw")
elif (computer == 0 and guess == 2) or (computer == 1 and guess == 0) or \
        (computer == 2 and guess == 1):
    print("The computer is", computerName, ". You are", guessName, ". You lose")
elif (computer == 2 and guess == 0) or (computer == 0 and guess == 1) or \
        (computer == 1 and guess == 2):
    print("The computer is", computerName, ". You are ", guessName, ". You won")
