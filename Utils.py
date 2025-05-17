import os

# Constants
SCORES_FILE_NAME = "Scores.txt"
BAD_RETURN_CODE = -1

# Function to clear the screen
def screen_cleaner():
    os.system('cls' if os.name == 'nt' else 'clear')
