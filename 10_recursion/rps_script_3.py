""" RPS simple game, version 3 """

# import numbers
# import sys
import random
from enum import Enum


def play_rps():
    """" Play RPS func """
    class RPS(Enum):
        """Class representing Rock Paper Scissor enumeration value"""
        ROCK = 1
        PAPER = 2
        SCISSORS = 3

    quit_message = '\nThank you for playing our game !\n'
    value_error_message = "ERROR : Invalid input. Please enter 1, 2 or 3"
    victory = "YOU WIN !"

    player_choice = input("\nEnter a choice...\n1.Rock  \n2.Paper \n3.Scissor \n4.Quit game "
                          "\n\n")
    if player_choice == 'quit':
        print(quit_message)
        return
    try:
        player_choice = int(player_choice)
    except ValueError:
        if player_choice not in [1, 2, 3, 4]:
            print(value_error_message)
            return play_rps()

    if player_choice == 4:
        print(quit_message)
        return

    computer_choice = int(random.choice("123"))

    print("You chose: " + str(RPS(player_choice).name) + ".")
    print("Computer chose: " + str(RPS(computer_choice).name) + ".")

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

    play_rps()


play_rps()
