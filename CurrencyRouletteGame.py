'''
This game will use the free currency api to get the current exchange rate from USD to ILS, will
generate a new random number between 1-100 a will ask the user what he thinks is the value of
the generated number from USD to ILS, depending on the user’s difficulty his answer will be
correct if the guessed value is between the interval surrounding the correct answer
Properties
1. Difficulty
Methods
1. get_money_interval -Will get the current currency rate from USD to ILS and will
generate an interval as follows:
a. for given difficulty d, and total value of money t the interval will be: (t - (5 - d), t +
(5 - d))
2. get_guess_from_user - A method to prompt a guess from the user to enter a guess of
value to a given amount of USD
3. play - Will call the functions above and play the game. Will return True / False if the user
lost or won.


'''

import requests

base_url = "https://v6.exchangerate-api.com/v6/6e727c5778a4ba02f5d3ac37/latest"

def get_money_interval(base_currency):
    base_currency = base_currency.upper()
    url = f"{base_url}/{base_currency}"  # Correct URL format
    response = requests.get(url)

    if response.status_code == 200:
        currency_data = response.json()
        return currency_data
    else:
        print(f"Failed to retrieve data. HTTP Status: {response.status_code}")
        return None



# if currency_info:
#     ils_rate = currency_info["conversion_rates"]["ILS"] 
#     print(f"Exchange rate from {base_currency} to ILS: {ils_rate}")


def get_guess_from_user(Difficulty, base_currency, ils_rate):
    """Prompts the user for a number between 1 and Difficulty, ensuring valid input."""
    try:
        guess = float(input(f"Guess the currency rate of {base_currency} to ILS: "))
        if (ils_rate - (5 - Difficulty)) <= guess <= (ils_rate + (5 - Difficulty)):
            return guess  # Return the valid guess
            
    except ValueError:
        print("Invalid input. Please enter a numeric value.")


def play(Difficulty):
    """Starts the game and determines if they won."""
    #Difficulty = 2  # Set the difficulty level (can be changed dynamically)

    for attempt in range(3):  # Allow up to 3 attempts
        base_currency = "USD"
        currency_info = get_money_interval(base_currency)
        ils_rate = currency_info["conversion_rates"]["ILS"]
        #get_guess_from_user(Difficulty, base_currency, ils_rate)
        print(ils_rate)
        print((ils_rate - (5 - Difficulty)))
        print((ils_rate + (5 - Difficulty)))


        if get_guess_from_user(Difficulty, base_currency, ils_rate):
            print("Congratulations! You guessed correctly. 🎉")
            return True
        else:
            print(f"Sorry, wrong guess. You have {2 - attempt} attempts left. ❌")

    # If the loop finishes without a correct guess, return False
    print("Game over. You have used all attempts. ❌")
    return False

# Run the game
#play()
