from art import rock, paper, scissors
import random

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors.\n"))

comp_choice = random.randint(0, 2)

game_images = [rock, paper, scissors]

if user_choice == 0 and comp_choice == 2:
    print("You chose:\n{}".format(game_images[user_choice]))
    print("Computer chose:\n{}".format(game_images[comp_choice]))
    print("You Won")
elif user_choice == 2 and comp_choice == 1:
    print("You chose:\n{}".format(game_images[user_choice]))
    print("Computer chose:\n{}".format(game_images[comp_choice]))
    print("You Won")
elif user_choice == 1 and comp_choice == 0:
    print("You chose:\n{}".format(game_images[user_choice]))
    print("Computer chose:\n{}".format(game_images[comp_choice]))
    print("You Won")
elif user_choice == comp_choice:
    print("You chose:\n{}".format(game_images[user_choice]))
    print("Computer chose:\n{}".format(game_images[comp_choice]))
    print("Tie!! Try again")
else:
    print("You chose:\n{}".format(game_images[user_choice]))
    print("Computer chose:\n{}".format(game_images[comp_choice]))
    print("Computer Won")
