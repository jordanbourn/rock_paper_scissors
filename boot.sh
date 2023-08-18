#! /bin/bash

# For this assignment, write a .sh file called `boot.sh`. In the same directory as boot.sh, create a Python
# file that plays a game of rock paper scissors. Use boot.sh to ask users if they'd like to play rock paper scissors;
# if they answer 'yes', then execute the Python file. If not, have the shell file tell users 'That's too bad,
# maybe next time'.
# It is common to use Shell scripts to boot entire applications; this is a very small version of that same concept.
# The notion document attached comes courtesy of Coding Temple's very own Derek Hawkins and covers similar topics.
# Upload your Python and your shell script to Github, and post the repo link here.

# Ask user if they would like to play
echo Hello! Would you like to play Rock Paper Scissors? yes/no
read user_input
# if 'yes' run rock paper scissors, if 'no' say goodbye
if [ $user_input == "yes" ]
then
    python3 rps.py
else
    echo "That's too bad, maybe next time. Goodbye!"
fi