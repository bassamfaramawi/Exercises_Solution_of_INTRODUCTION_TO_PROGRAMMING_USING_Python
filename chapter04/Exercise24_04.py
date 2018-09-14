'''
**4.24 (Game: pick a card ) Write a program that simulates picking a card from a deck of
52 cards. Your program should display the rank (Ace, 2, 3, 4, 5, 6, 7, 8, 9, 10,
Jack, Queen, King) and suit (Clubs, Diamonds, Hearts, Spades) of the card.

/**
 * @author BASSAM FARAMAWI
 * @email tiodaronzi3@yahoo.com
 * @since 2018
 */
'''
import random

# Randomly generate the card rank number
rank = random.randint(1, 13)

# Randomly generate the card suit number
suit = random.randint(1, 4)

# Assign rank name based on rank number generated
if rank == 1:
    rankName = "Ace"
elif rank == 2:
    rankName = "2"
elif rank == 3:
    rankName = "3"
elif rank == 4:
    rankName = "4"
elif rank == 5:
    rankName = "5"
elif rank == 6:
    rankName = "6"
elif rank == 7:
    rankName = "7"
elif rank == 8:
    rankName = "8"
elif rank == 9:
    rankName = "9"
elif rank == 10:
    rankName = "10"
elif rank == 11:
    rankName = "Jack"
elif rank == 12:
    rankName = "Queen"
elif rank == 13:
    rankName = "King"

# Assign suit name based on suit number generated
if suit == 1:
    suitName = "Clubs"
elif suit == 2:
    suitName = "Diamonds"
elif suit == 3:
    suitName = "Hearts"
elif suit == 4:
    suitName = "Spades"

# Display the result
print("The card you picked is", rankName, "of", suitName)
