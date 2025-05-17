from Live import load_game, welcome
from Scores import add_score

# Import game modules (each must expose play(difficulty) -> bool)
import GuessGame
import MemoryGame
import CurrencyRouletteGame


def main():
    # Greet the user and get their name
    name = welcome()

    # Let the user choose a game and difficulty
    game_choice, game_difficulty = load_game()

    if not (game_choice and game_difficulty):
        # Invalid selections already handled inside load_game()
        return

    print(f"Hello {name}, you chose game {game_choice} with difficulty {game_difficulty}!\n")

    # Map each game number to its corresponding module
    game_dispatch = {
        1: MemoryGame,
        2: GuessGame,
        3: CurrencyRouletteGame,
    }

    selected_game = game_dispatch.get(game_choice)

    if not selected_game:
        print("Invalid game choice. Exiting.")
        return

    # Run the selected game. The play() function must return True on win, False otherwise.
    try:
        did_win = selected_game.play(game_difficulty)
    except AttributeError:
        print(f"The selected game module ({selected_game.__name__}) does not implement play(). Exiting.")
        return

    # Update the score if the player won
    if did_win:
        add_score(game_difficulty)
        print("Congratulations! Your score has been updated.")
    else:
        print("Better luck next time – no score change.")


if __name__ == '__main__':
    main()
