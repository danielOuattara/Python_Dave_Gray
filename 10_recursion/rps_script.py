import numbers
import sys
import random
from enum import Enum


def play_rps():
    class RPS(Enum):
        ROCK = 1
        PAPER = 2
        SCISSORS = 3

    player_choice = 0
    quit_message = 'Thank you for playing our game !'

    player_choice = input("Enter your choice...\n1.Rock  \n2.Paper \n3.Scissor \n4.To quit the game "
                          "\n\n")
    if player_choice == 'quit':
        print(quit_message)
        return
    try:
        player_choice = int(player_choice)
    except:
        if player_choice not in [1, 2, 3, 4]:
            sys.exit("Invalid input. Please enter 1, 2 or 3")

    if player_choice == 4:
        print(quit_message)
        return
    computer_choice = int(random.choice("123"))

    print("You chose: " + str(RPS(player_choice).name) + ".")
    print("Computer chose: " + str(RPS(computer_choice).name) + ".")

    if player_choice == 1 and computer_choice == 3:
        print("you win !")
    elif player_choice == 2 and computer_choice == 1:
        print("you win !")
    elif player_choice == 3 and computer_choice == 2:
        print("you win !")
    elif player_choice == computer_choice:
        print("Tie Game !")
    else:
        print("Computer Win!")

    print('Play again ! ')

    play_rps()


play_rps()
