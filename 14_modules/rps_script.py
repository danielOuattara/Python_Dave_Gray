import random
from enum import Enum


def rps_game():
    game_count = 0
    player_score = 0
    computer_score = 0

    def play_rps():
        nonlocal game_count, player_score, computer_score

        class RPS(Enum):
            ROCK = 1
            PAPER = 2
            SCISSORS = 3

        quit_message = f"Thank you for playing our game !\nYou played : {game_count} times "
        print('~' * 30)

        player_choice = input(f"\nEnter your choice...\n1.Rock  \n2.Paper \n3.Scissor \n4.To quit the game\n").strip()

        if player_choice == 'quit' or player_choice == 'q':
            print(quit_message)
            return

        try:
            player_choice = int(player_choice)
            if player_choice not in [1, 2, 3, 4]:
                raise ValueError("Invalid input. Please enter 1, 2, 3, or 4")
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
                return "You win !"

            elif player == computer:
                return "Tie Game !"
            else:
                computer_score += 1
                return "Computer Win!"

        result = decide_winner(player_choice, computer_choice)
        print(result)
        game_count += 1
        print('Game Count = ', game_count)
        print('Player Score = ', player_score)
        print('Computer Score = ', computer_score)

        print('Play again ! ')
        play_rps()

    return play_rps


rock_paper_scissors = rps_game()

if __name__ == '__main__':
    rock_paper_scissors()
