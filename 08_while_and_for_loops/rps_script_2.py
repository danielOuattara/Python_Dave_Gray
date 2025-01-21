""" RPS simple game, version 2 """

import sys
import random
from enum import Enum


class EnumRPS(Enum):
    """Class representing Rock Paper Scissor enumeration value"""
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


player_choice = 0
quit_message = '\nThank you for playing our game !\n'
value_error_message = "ERROR : Invalid input. Please enter 1, 2 or 3"
victory = "YOU WIN !"

while True:
    player_choice = input("\nEnter a choice...\n1.Rock  \n2.Paper \n3.Scissor \n4.Quit game "
                          "\n\n")
    if player_choice == 'quit':
        print(quit_message)
        break
    try:
        player_choice = int(player_choice)
    except ValueError:
        print(value_error_message)
        continue

    if player_choice < 1 or player_choice > 4:
        sys.exit(value_error_message)

    if player_choice == 4:
        print(quit_message)
        break

    computer_choice = int(random.choice("123"))

    print("You chose: " + str(EnumRPS(player_choice).name) + ".")
    print("Computer chose: " + str(EnumRPS(computer_choice).name) + ".")

    if player_choice == 1 and computer_choice == 3:
        print(victory)
    elif player_choice == 2 and computer_choice == 1:
        print(victory)
    elif player_choice == 3 and computer_choice == 2:
        print(victory)
    elif player_choice == computer_choice:
        print("TIE GAME !")
    else:
        print("COMPUTER WIN !")

    print('\n-------\nPlay again ! ')
