# For this assignment, write a .sh file called `boot.sh`. In the same directory as boot.sh, create a Python file
# that plays a game of rock paper scissors. Use boot.sh to ask users if they'd like to play rock paper scissors;
# if they answer 'yes', then execute the Python file. If not, have the shell file tell users 'That's too bad,
# maybe next time'.
# It is common to use Shell scripts to boot entire applications; this is a very small version of that same concept.
# The notion document attached comes courtesy of Coding Temple's very own Derek Hawkins and covers similar topics.
# Upload your Python and your shell script to Github, and post the repo link here.

import random

while True:
    user_play = input("Rock, Paper, Scissors?  Enter QUIT to exit the game.\n")
    possible_actions = ["rock", "paper", "scissors"]
    comp_play = random.choice(possible_actions)
    print(f"\nYou chose {user_play}, computer chose {comp_play}.\n")

    if user_play.lower() == comp_play:
        print(f"Both players selected {user_play}. It's a tie!")
    elif user_play.lower() == "quit":
        print("We can play again another time. Goodbye!")
        break
    elif user_play.lower() == "rock":
        if comp_play == "scissors":
            print("You win!")
        else:
            print("You lose.")
    elif user_play.lower() == "paper":
        if comp_play == "rock":
            print("You win!")
        else:
            print("You lose.")
    elif user_play.lower() == "scissors":
        if comp_play == "paper":
            print("You win!")
        else:
            print("You lose.")

    play_again = input("Would you like to play again? (y/n): ")
    if play_again.lower() != "y":
        print("Thanks for playing! Goodbye!")
        break
