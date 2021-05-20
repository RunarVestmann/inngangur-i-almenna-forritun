import random

choices = ["rock", "paper", "scissors"]

pc_choice = choices[random.randint(0, len(choices)-1)]

user_choice = input("Enter your choice: ")

if user_choice in choices:
    print(f"Computer's choice: {pc_choice}")

    if user_choice == "rock":
        if pc_choice == "scissors":
            print("You won")
        elif pc_choice == "paper":
            print("You lost")
        else:
            print("It's a tie")
    elif user_choice == "paper":
        if pc_choice == "rock":
            print("You won")
        elif pc_choice == "scissors":
            print("You lost")
        else:
            print("It's a tie")
    elif user_choice == "scissors":
        if pc_choice == "paper":
            print("You won")
        elif pc_choice == "rock":
            print("You lost")
        else:
            print("It's a tie")
else:
    print("Invalid input, please enter one of the following: rock, paper or scissors")
