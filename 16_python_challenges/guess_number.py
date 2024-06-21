import argparse
import random
import cla_parser


def guess_number_game(name="Player 1"):
    game_count = 0
    player_score = 0

    def play_guess_number():
        print('~' * 30)
        nonlocal game_count, player_score, name

        valid_numbers = [1, 2, 3]
        quit_message = f"Thank you for playing!\nBye {name}! "
        player_choice = int(input(f"{name}, guess which number I'm thinking of...: 1, 2 or 3 ?\n\n").strip())

        # try:
        #     player_choice = int(player_choice)
        #     if player_choice not in valid_numbers:
        #         raise ValueError(f"{name}, please enter 1, 2 or 3.")
        #
        # except ValueError as e:
        #     print(e)
        #     play_guess_number()
        #     return

        computer_choice = random.choice(valid_numbers)

        def is_player_win(player, computer):
            nonlocal player_score

            if player == computer:
                player_score += 1
                return f'\n{name} you win!\n'
            else:
                return f'\nSorry, {name}. Better luck next time :(\n'

        game_message = f'\n{name}, you chose {player_choice}.\nI was thinking about the number {computer_choice}'
        game_result = is_player_win(player_choice, computer_choice)
        game_count += 1

        print(game_message)
        print(game_result)

        print('Game Count : ', game_count)
        print(f"{name}'s Score : ", player_score)
        print(f"Your winning percentage: {player_score / game_count:.2%}")

        play_again = input(f'\nPlay again, {name} ? '
                           f'\n\nY for Yes or '
                           f'\n\nQ to Quit\n')

        if play_again.lower() == 'y':
            play_guess_number()
        elif play_again.lower() == 'q':
            print(quit_message)
            return
        else:
            print("invalid input")
            return

    return play_guess_number


run_guess_number_game = guess_number_game(cla_parser.cla_parser())
run_guess_number_game()

"""
python3 guess_number.py -n Dave

Dave, guess which number I'm thinking of...: 1, 2 or 3 ?

1

Dave, you chose 1.
I was thinking about the number 1.

Dave, you win!

Game count: 1
Dave's score: 1
Your winning percentage: 100.00%

Play again, Dave ?
Y for Yes or
Q to Quit

------

Y

Dave, guess which number I'm thinking of...: 1, 2 or 3 ?

2

Dave, you chose 2.
I was thinking about the number 1.

Sorry, Dave. Better luck next time :(

Game count: 2
Dave's wins: 1
Your winning percentage: 50.00%

Play again, Dave ?
Y for Yes or
Q to Quit
-----
Y

Dave, guess which number I'm thinking of...: 1, 2 or 3 ?

5

Dave, please enter 1, 2 or 3.
----

Dave, guess which number I'm thinking of...: 1, 2 or 3 ?

Play again, Dave ?
Y for Yes or
Q to Quit

Q

Thank you for playing!
Bye Dave!
"""
