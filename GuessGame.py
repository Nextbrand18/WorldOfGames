"""
The purpose of guess game is to start a new game, cast a random number between 1 to a
variable called difficulty . The game will get a number input from the
Properties
1. Difficulty
2. Secret number

Methods
1. generate_number - Will generate number between 1 to difficulty and save it to
secret_number.
2. get_guess_from_user - Will prompt the user for a number between 1 to difficulty and
return the number.
3. compare_results - Will compare the the secret generated number to the one prompted
by the get_guess_from_user.
4. play - Will call the functions above and play the game. Will return True / False if the user
lost or won.

"""

import random

def generate_number(Difficulty):
    """Generates a random number between 1 and Difficulty."""
    return random.randint(1, Difficulty)

def get_guess_from_user(Difficulty):
    """Prompts the user for a number between 1 and Difficulty, ensuring valid input."""
    while True:
        try:
            guess = int(input(f"Input a number between 1 and {Difficulty}: "))
            if 1 <= guess <= Difficulty:
                return guess  # Return the valid guess
            else:
                print("Invalid input. Please enter a number within the range.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def compare_results(secret_number, user_guess):
    """Compares the generated secret number with the user's guess."""
    return secret_number == user_guess

def play(Difficulty):
    """Starts the game, generates a number, gets user input, and determines if they won."""
    #Difficulty = 10  # Set the difficulty level (can be changed dynamically)

    for attempt in range(3):  # Allow up to 3 attempts
        secret_number = generate_number(Difficulty)
        user_guess = get_guess_from_user(Difficulty)

        # Uncomment the next two lines to see the secret number and user's guess (for testing)
        # print(f"Secret number: {secret_number}")
        # print(f"Your guess: {user_guess}")

        if compare_results(secret_number, user_guess):
            print("Congratulations! You guessed correctly. 🎉")
            return True
        else:
            print(f"Sorry, wrong guess. You have {2 - attempt} attempts left. ❌")

    # If the loop finishes without a correct guess, return False
    print("Game over. You have used all attempts. ❌")
    return False

# Run the game
#play(Difficulty)
