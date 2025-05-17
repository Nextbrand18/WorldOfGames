"""
MemoryGame.py
The purpose of memory game is to display an amount of random numbers to the users for 0.7
seconds and then prompt them from the user for the numbers that he remember. If he was right
with all the numbers the user will win otherwise he will lose.
Properties
1. Difficulty
Methods
1. generate_sequence - Will generate a list of random numbers between 1 to 101. The list
length will be difficulty .
2. get_list_from_user - Will return a list of numbers prompted from the user. The list length
will be in the size of difficulty .
3. is_list_equal - A function to compare two lists if they are equal. The function will return
True / False.
4. play - Will call the functions above and play the game. Will return True / False if the user
lost or won.

"""
import random
import time

a = []
def generate_sequence(Difficulty):
    for item in range(Difficulty):

        a.append(random.randint(1, 101) )
    return a



def display_list_for_duration(values, duration=0.7):
    for value in values:
        print(value, end="\r", flush=True)  # Print the value and overwrite the previous one
        time.sleep(duration)



def get_list_from_user(Difficulty):
    num_list = []  # Initialize an empty list
    
    # Prompt the user to enter up to 4 numbers
    for i in range(Difficulty):
        try:
            user_input = int(input(f"Enter number {i+1} (of {Difficulty}): "))
            num_list.append(user_input)
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue
    return num_list
    #print(f"Your list of numbers: {num_list}")

def is_list_equal(seq, ilist):
    if seq == ilist:
        return True
    else:
        return False
    


# seq = generate_sequence(dif)
# display_list_for_duration(seq)
# # print(seq)

# ilist = get_list_from_user(dif)
# #print(ilist)

def play(Difficulty):
    """Starts the game, generates a number, gets user input, and determines if they won."""
    #Difficulty = 2   # Set the difficulty level (can be changed dynamically)

    for attempt in range(3):  # Allow up to 3 attempts
        seq = generate_sequence(Difficulty)
        display_list_for_duration(seq)
        ilist = get_list_from_user(Difficulty)

        # Uncomment the next two lines to see the secret number and user's guess (for testing)
        # print(f"Secret number: {secret_number}")
        # print(f"Your guess: {user_guess}")

        if is_list_equal(seq, ilist):
            print("Congratulations! You guessed correctly. 🎉")
            return True
        else:
            print(f"Sorry, wrong guess. You have {2 - attempt} attempts left. ❌")

    # If the loop finishes without a correct guess, return False
    print("Game over. You have used all attempts. ❌")
    return False

# Run the game
#play(Difficulty)