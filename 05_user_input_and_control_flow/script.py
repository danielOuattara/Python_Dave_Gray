import sys
import random
from enum import Enum


class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


# print(RPS(2))
# print(RPS.ROCK)
# print(RPS['ROCK'])
# print(RPS.ROCK.value)
# print(RPS.ROCK.name)
# sys.exit()

print("")

player_choice = 0
try:
    player_choice = int(
        input("Enter your choice...\n1.Rock  \n2.Paper \n3.Scissor \n\n"))

except:
    if player_choice < 1 or player_choice > 3:
        sys.exit("Invalid input. Please enter 1, 2 or 3")

computer_choice = int(random.choice("123"))

print("You chose: " + str(RPS(player_choice).name) + ".")
print("Computer chose: " + str(RPS(computer_choice).name) + ".")
print("")

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
