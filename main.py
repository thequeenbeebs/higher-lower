from game_data import data
import art
import random
from replit import clear

def generate_random_account():
    return(random.choice(data))

def compare(guess, followers_a, followers_b):
    winner = ""
    if followers_a > followers_b:
        winner = 'A'
    else:
        winner = 'B'
    if winner == guess:
        return "Correct"
    else:
        return "Incorrect"

def play_game():
    person_a = generate_random_account()
    person_b = generate_random_account()
    result = ""
    game_over = False
    user_score = 0
    
    while not game_over:
        clear()
        print(art.logo)

        if result == "Correct":
            user_score += 1
            print(f"You're right! Current score: {user_score}")
        elif result == "Incorrect":
            print(f"Sorry, that's wrong. Final score: {user_score}")
            return

        print(f"Compare A: {person_a['name']}, a {person_a['description']}, from {person_a['country']}.")
        print(art.vs)
        print(f"Against B: {person_b['name']}, a {person_b['description']}, from {person_b['country']}.")
        guess = input("Who has more followers? Type 'A' or 'B': ")
        result = compare(guess, person_a['follower_count'], person_b['follower_count'])
        person_a = person_b
        person_b = generate_random_account()
    


play_game()