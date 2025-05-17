
"""
welcome(name)
This function has a person name as an input and returns a string in the following layout:
Hello <name> and welcome to the World of Games (WoG).
Here you can find many cool games to play.

"""
'''
def welcome():
    name = input("Please enter your name: ")
    print (f"Hello {name} and welcome to the World of Games (WoG).\n" "Here you can find many cool games to play.")
    print ("\n")

welcome()
'''

def welcome():
    # Prompt user for their name
        name = input("Please enter your name: ")
        xlen = len(name)

        # Check if the name is empty
        if not name:
            print("Name cannot be empty. Please enter your name.")
            welcome()

        elif xlen < 6:
            print("You have entered fewer character. Minimum character lenght is 6.")
            welcome()
        else:
            print (f"Hello {name} and welcome to the World of Games (WoG).\n" "Here you can find many cool games to play.")
            print ("\n")
        return name
            



"""
load_game()
This function prints out the following text:
Please choose a game to play:
1. Memory Game - a sequence of numbers will appear for 1 second and you have to
guess it back
2. Guess Game - guess a number and see if you chose like the computer
3. Currency Roulette - try and guess the value of a random amount of USD in ILS
Gets an input from the user about the game he chose. After receiving the game number from
the user, the function will get the level of difficulty with the following text and also save to a
variable:
Please choose game difficulty from 1 to 5:
The function will check the input of the chosen game (the input suppose to be a number
between 1 to 3), also will check the input of level of difficulty (input should be a number between
1 to 5).
"""

def load_game():
    # Allow up to 3 attempts for game selection
    for attempt in range(3):
        try:
            game_choice = int(input(
                "Please choose a game to play: \n"
                "1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back\n"
                "2. Guess Game - guess a number and see if you chose like the computer\n"
                "3. Currency Roulette - try and guess the value of a random amount of USD in ILS\n"
                "Your selection: "
            ))
            if 1 <= game_choice <= 3:
                break  # Exit loop if valid input
            else:
                print(f"Invalid choice. Attempts left: {2 - attempt}")
        except ValueError:
            print(f"Invalid input. Please enter a number. Attempts left: {2 - attempt}")
    else:
        print("Too many failed attempts. Exiting...")
        return None, None  # Exit function with failure state

    # Allow up to 3 attempts for difficulty selection
    for attempt in range(3):
        try:
            game_difficulty = int(input("Please choose game difficulty from 1 to 5: "))
            if 1 <= game_difficulty <= 5:
                #print(f"You chose game {game_choice} with difficulty {game_difficulty}!")
                return game_choice, game_difficulty  # Return valid values
            else:
                print(f"Invalid difficulty. Attempts left: {2 - attempt}")
        except ValueError:
            print(f"Invalid input. Please enter a number. Attempts left: {2 - attempt}")
    else:
        print("Too many failed attempts. Exiting...")
        return None, None  # Exit function with failure state


def main():
    welcome()
    load_game()                



if __name__ == '__main__':
    main()               


# # Example usage:
# game, difficulty = load_game()
# if game is not None and difficulty is not None:
#     print(f"Game: {game}, Difficulty: {difficulty}")
# else:
#     print("Failed to select a game. Please try again later.")