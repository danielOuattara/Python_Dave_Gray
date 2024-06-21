from enum import Enum
import random


def rps_game(name="Player_One"):
    game_count = 0
    player_score = 0
    computer_score = 0

    def play_rps():
        nonlocal game_count, player_score, computer_score, name

        class RPS(Enum):
            ROCK = 1
            PAPER = 2
            SCISSORS = 3

        quit_message = f"Thank you {name} for playing our game !\n{name} played : {game_count} times "
        print('~' * 30)

        player_choice = (input(f""
                               f"\nWelcome {name} !"
                               f"\nPlease, enter your choice..."
                               f"\n1.Rock  "
                               f"\n2.Paper "
                               f"\n3.Scissor "
                               f"\n4.q OR quit \n")
                         .strip())

        if player_choice == 'quit' or player_choice == 'q':
            print(quit_message)
            return

        try:
            player_choice = int(player_choice)
            if player_choice not in [1, 2, 3, 4]:
                raise ValueError(f"{name} your input is invalid.\nPlease enter 1, 2, 3, or 4")
        except ValueError as e:
            print(e)
            play_rps()
            return

        if player_choice == 4:
            print(quit_message)
            return

        computer_choice = random.choice(list(RPS))

        print(f"You chose:  {RPS(player_choice).name}")
        print(f"Computer chose:  {RPS(computer_choice).name}")

        def decide_winner(player, computer):
            nonlocal player_score, computer_score

            if (
                    player == 1 and computer == 3 or
                    player == 2 and computer == 1 or
                    player == 3 and computer == 2
            ):
                player_score += 1
                return f"You win {name} !"

            elif player == computer:
                return "Tie Game !"
            else:
                computer_score += 1
                return "Computer Win!"

        result = decide_winner(player_choice, computer_choice)
        print(result)
        game_count += 1
        print('Game Count = ', game_count)
        print(f'{name} Score = ', player_score)
        print('Computer Score = ', computer_score)

        print(f'Play again {name} ? ')
        play_rps()

    return play_rps


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description="Provide a personalized game experience.")
    parser.add_argument(
        "-n", "--name",
        metavar="name",
        required=True,
        help="The name of the person playing the game"
    )
    args = parser.parse_args()

    rock_paper_scissors = rps_game(args.name)
    rock_paper_scissors()
