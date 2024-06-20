import numbers
import sys
import random
from enum import Enum

game_count = 0


def play_rps():
    class RPS(Enum):
        ROCK = 1
        PAPER = 2
        SCISSORS = 3

    global game_count
    quit_message = f"Thank you for playing our game !\nYou played : {game_count} times "
    player_choice = input('~' * 30 + "\nEnter your choice...\n1.Rock  \n2.Paper \n3.Scissor \n4.To quit the game "
                                     "\n\n")
    if player_choice == 'quit' or 'q':
        print(quit_message)
        return
    try:
        player_choice = int(player_choice)
    except:
        if player_choice not in [1, 2, 3, 4]:
            print("Invalid input. Please enter 1, 2 or 3")
            play_rps()

    if player_choice == 4:
        print(quit_message)
        return
    computer_choice = int(random.choice("123"))

    print("You chose: " + str(RPS(player_choice).name) + ".")
    print("Computer chose: " + str(RPS(computer_choice).name) + ".")

    def decide_winner(player, computer):
        if player == 1 and computer == 3:
            return "You win !"
        elif player == 2 and computer == 1:
            return "You win !"
        elif player == 3 and computer == 2:
            return "You win !"
        elif player == computer:
            return "Tie Game !"
        else:
            return "Computer Win!"

    result = decide_winner(player_choice, computer_choice)
    print(result)
    game_count += 1
    print('game_count = ', game_count)

    print('Play again ! ')

    play_rps()


play_rps()
