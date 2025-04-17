# 1. TODO : write a function to compare A and B
# 2. TODO : move B to position of A if the user get's it right
# 3. TODO : keep the score counting if right
# 4. TODO : When wrong, print out that's wrong and final score
# 5. TODO :
# 6. TODO :
# 7. TODO :
from Game_data import data
from art import vs
from art import logo
import random



def random_game_data():
    """Pick and return a random character from data."""
    return random.choice(data)

def format_character(character):
    """Return a formatted string for display."""
    return f"{character['name']}, a {character['description']}, from {character['country']}"


def number_guessing_game():
    print(logo)
    current_score = 0

    character1 = random_game_data()
    character2 = random_game_data()
    while character1 == character2:
        character2 = random_game_data()

    gaming = True
    while gaming:
        print(f"Compare A: {format_character(character1)} \n")
        print(vs + "\n")
        print(f"Against B: {format_character(character2)} \n")

        user_guess = input("Who has more followers: "
                           "Type 'A' or 'B': ").lower()

        follower1 = character1['follower_count']
        follower2 = character2['follower_count']

        is_correct = False
        if user_guess == "a":
            is_correct = follower1 > follower2
        elif user_guess == "b":
            is_correct = follower2 > follower1

        if is_correct:
            current_score+=1
            print(f"You're right! Current score: {current_score}")
            character1 = character2
            character2 = random_game_data()
            while character1 == character2:
                character2 = random_game_data()

        else:
            print(f"❌ Sorry, that's wrong. Final score: {current_score}")
            gaming = False

play_game = True
while play_game:
    question = input("Type 'y' to play 'The Higher Lower Game' or "
                     " 'n' to exit: ").lower()
    if question == "y":
        number_guessing_game()
        question2 = input("Will you like to play again?. Type"
                          "'y' for yes and 'n' for no: ").lower()
        if question2 == "y":
            number_guessing_game()
        else:
            print("Thank you for playing!")
            play_game= False
    else:
        print("Well noted!")
        play_game = False
