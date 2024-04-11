from game_data import data
from art import logo, vs
import random
import os



def check_guess(guess, a_followers, b_followers):


    if a_followers > b_followers:
        return guess == 'A'
    else:
        return guess == 'B'

def get_random_choice():
    """Pick a random choice from the data"""
    return random.choice(data)

def format_data(choice):
  """Format account into printable format: name, description and country"""
  name = choice["name"]
  description = choice["description"]
  country = choice["country"]
  # print(f'{name}: {account["follower_count"]}')
  return f"{name}, a {description}, from {country}"



def game():
    game_over = False
    score = 0
    print (logo)
    choice_a = get_random_choice()
    choice_b = get_random_choice()

    while not game_over:
        choice_a = choice_b
        choice_b = get_random_choice()

        while choice_a == choice_b:
            choice_b = get_random_choice()


        print(f"Compare A: {format_data(choice_a)}.")
        print(vs)
        print(f"Against B: {format_data(choice_b)}.")
        
        guess = input("Who has more followers? Type 'A' or 'B': ")
        a_follower_count = choice_a["follower_count"]
        b_follower_count = choice_b["follower_count"]
        is_correct = check_guess(guess, a_follower_count, b_follower_count)
        if is_correct:
            print (f"Correct! Current score: {score}")
            score +=1
        else:
            os.system('clear') # Clear the screen
            print(logo)
            print(f'Sorry thats wrong. Final score: {score}')
            game_over = True



game()