from Utils import SCORES_FILE_NAME
import os

def add_score(difficulty):
    try:
        score_to_add = (difficulty * 3) + 5
        current_score = 0

        # Read current score if file exists
        if os.path.exists(SCORES_FILE_NAME):
            with open(SCORES_FILE_NAME, 'r') as file:
                content = file.read().strip()
                if content.isdigit():
                    current_score = int(content)

        # Update score
        new_score = current_score + score_to_add

        # Write updated score
        with open(SCORES_FILE_NAME, 'w') as file:
            file.write(str(new_score))

    except Exception as e:
        print(f"Error updating score: {e}")

