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
    num_of_tries = 0

    # Create and initialize a number of tries list
    num_of_tries_list = []

    # Game loop
    while user_guess != random_number:

        # Prompt user for input
        try:
            user_guess = int(input("Please enter a number between 1 and 10: "))
            if user_guess == 0 or user_guess > 10:
                raise ValueError
        except ValueError:
            print("Please enter a number between 1 and 10 inclusive!")

        else:
            num_of_tries += 1
            if user_guess < random_number:
                print(f"The number {user_guess} is lower than the secret number! Please try again...")

            elif user_guess > random_number:
                print(f"The number {user_guess} is higher than the secret number! Please try again...")

            else:
                print(f"Congratulations!!! You guessed the right number in {num_of_tries} tries.")
                num_of_tries_list.append(num_of_tries)

        while user_guess == random_number:
                try_again = input("Do you wanna try again? (Y/N) : ")
                if try_again == "Y" or try_again == "y" or try_again == "yes".lower():
                    user_guess = 0
                    num_of_tries = 0
                    random_number = random.randint(1, 10)
                    print(f"The record so far is {min(num_of_tries_list)} tries. Try to beat that!")
                    break
                elif try_again == "":
                    print("Please either type 'yes' or 'no'")
                    continue

                else:
                    print("Thanks for playing!")
                    print(f"The mean of the saved attempts list is {statistics.mean(num_of_tries_list)}")
                    print(f"The median of the saved attempts list is {statistics.median(num_of_tries_list)}")
                    print(f"The mode of the saved attempts list is {statistics.mode(num_of_tries_list)}")
                    print("We hope to see you soon!")
                    break


if __name__ == "__main__":
    start_game()
