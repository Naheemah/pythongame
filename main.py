import random

while True:
    user_action = input("Enter a choice (R, P, S): ")
    possible_actions = ["R", "P", "S"]
    computer_action = random.choice(possible_actions)
    print(f"\nPlayer: {user_action}, CPU: {computer_action}.\n")

    if user_action == computer_action:
        print(f"Both players selected {user_action}. It's a tie!")
    elif user_action == "R":
        if computer_action == "S":
            print("Rock beats Scissors! You win!")
        else:
            print("Paper beats Rock! You lose.")
    elif user_action == "P":
        if computer_action == "R":
            print("Paper beats Rock! You win!")
        else:
            print("Scissors beats Paper! You lose.")
    elif user_action == "S":
        if computer_action == "P":
            print("Scissors beats Paper! You win!")
        else:
            print("Rock beats Scissors! You lose.")
    else:
        print("Enter a valid input")

    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        break