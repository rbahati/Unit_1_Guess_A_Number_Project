# Importing the random library

import random

# Importing the statistics library

import statistics


def start_game():
    """This function is the entry point for the game"""

    print("WELCOME TO THE NUMBER GUESSING GAME!!!\nLet's see in how many tries you will guess the number.\nHave Fun!!!")

    # Generate a random number
    random_number = random.randint(1, 10)

    # Create and initialize a user guess variable
    user_guess = 0

    # Create and initialize a number of tries variable
    num_of_tries = 1

    # Game loop
    while user_guess != random_number:

        # Prompt user for input
        user_guess = int(input("Please enter a number between 1 and 10: "))
        if user_guess < random_number:
            print(f"The number {user_guess} is lower than the secret number! Please try again...")
            num_of_tries += 1
        elif user_guess > random_number:
            print(f"The number {user_guess} is higher than the secret number! Please try again...")
            num_of_tries += 1
        else:
            print(f"Congratulations!!! You guessed the right number in {num_of_tries} tries.")
            try_again = input("Do you wanna try again? (Y/N) : ")
            if try_again == "Y" or try_again == "y" or try_again == "yes".lower():
                user_guess = 0
                random_number = random.randint(1, 10)

            else:
                print("Thanks for playing!\nHope to see you soon!!!")
                break


if __name__ == "__main__":
    start_game()
