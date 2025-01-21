"""RPS simple game, version 1"""

import sys
import random
from enum import Enum


class EnumRPS(Enum):
    """Class representing Rock Paper Scissor enumeration value"""
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


# print(EnumRPS(2))
# print(EnumRPS.ROCK)
# print(EnumRPS['ROCK'])
# print(EnumRPS.ROCK.value)
# print(EnumRPS.ROCK.name)
# sys.exit()


player_choice = 0
try:
    player_choice = int(
        input("\nEnter your choice...\n1.Rock  \n2.Paper \n3.Scissor \n\n"))

except ValueError:
    if player_choice < 1 or player_choice > 3:
        sys.exit("Invalid input. Please enter 1, 2 or 3")

computer_choice = int(random.choice("123"))

print("You chose: " + str(EnumRPS(player_choice).name) + ".")
print("Computer chose: " + str(EnumRPS(computer_choice).name) + ".\n")

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
