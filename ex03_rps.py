import random

print("\n--------- START THE GAME --------- \n")

user_action = input("ENTER A CHOICE (ROCK / PAPER / SCISSORS): ")

possible_actions = ["ROCK", "PAPER", "SCISSORS"]
computer_action = random.choice(possible_actions)

print(f"\n➡️ YOU CHOSE {user_action}, COMPUTER CHOSE {computer_action}.\n")

if user_action == computer_action:
    print(f"\nBOTH PLAYERS SELECTED {user_action}. EQUALITY!\n")
elif user_action == "ROCK":
    if computer_action == "SCISSORS":
        print("\nROCK CRUSHES SCISSORS! YOU WIN!\n")
    else:
        print("\nPAPER COVERS ROCK! YOU LOSE.\n")
elif user_action == "PAPER":
    if computer_action == "ROCK":
        print("\nPAPER COVERS ROCK! YOU WIN!\n")
    else:
        print("\nSCISSORS CUTS PAPER! YOU LOSE.\n")
elif user_action == "SCISSORS":
    if computer_action == "PAPER":
        print("\nSCISSORS CUTS PAPER! YOU WIN!\n")
    else:
        print("\nROCK CRUSHES SCISSORS! YOU LOSE.\n")

