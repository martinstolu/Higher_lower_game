# TODO 1. Write a function extract the data
# TODO 2. function to compare the extracted data
# TODO 3. store the score and print it if user is right
#  and score += 1
# TODO 4.move b to a and print another data as b
# TODO 5.if wrong end the game and print the final score

from Game_data import data
import art
import time
import random



def random_game_data():
    """Pick and return a random character from data."""
    return random.choice(data)

def format_character(character):
    """Return a formatted string for display."""
    return (f"{character['name']}, a {character['description']},"
            f" from {character['country']}")

def get_unique_character(existing_character):
    """Return a unique character from data list"""
    new_character = random_game_data()
    while new_character == existing_character:
        new_character = random_game_data()
    return new_character

def display_characters(char_a, char_b):
    """Displays the print statement."""
    print(f"Compare A: {char_a['name']}, a {char_a['description']}, from {char_a['country']}.\n")
    print(f"{art.vs}\n")
    print(f"Against B: {char_b['name']}, a {char_b['description']}, from {char_b['country']}.\n")



def number_guessing_game():
    print(art.logo)
    current_score = 0

    character1 = random_game_data()
    character2 = get_unique_character(character1)

    gaming = True
    while gaming:

        time.sleep(1)

        follower1 = character1['follower_count']
        follower2 = character2['follower_count']

        display_characters(character1, character2)

        user_guess = input("Who has more followers: "
                           "Type 'A' or 'B': ").lower()

        is_correct = ((user_guess == "a"
                      and follower1 > follower2)
                      or (user_guess == "b"
                          and follower2 > follower1))

        time.sleep(1)

        if is_correct:
            current_score+=1
            print(f"You're right! Current score: {current_score}")
            character1 = character2
            character2 = get_unique_character(character1)

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