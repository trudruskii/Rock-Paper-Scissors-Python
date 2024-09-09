# SpencerP5.py
# Programmer: Andrew Spencer
# Email: aspencer22@cnm.edu
# Date: 09/07/2024
# Purpose: Create a program that will play a game of rock paper scissors with a user.
# The program keeps track of the user's score, the computer's score, the number of ties, and the number of rounds.
# The game continues until the user decides to stop playing.
# Python Version: 3.12.5

# import random module to generate random choices from the list
import random
# import time module to make program more interactive
import time

# Greet the user
print('Ready to play a game of rock, paper, scissors?')
print('To get started: ')

# Initialize variables for keeping score
user_score = 0
cpu_score = 0
rounds_played = 0
ties = 0

# Create a list of possible choices
choices = ["rock", "paper", "scissors"]

# Loop that continues until user decides to stop playing
while True:
    # Reinitialize the score variables if user decides to play again
    user_score = 0
    cpu_score = 0

    # Loop that continues until either the user or computer has won 2 games
    while user_score < 2 and cpu_score < 2:
        rounds_played += 1
        # Get user's choice to start game and convert it to lowercase for case insensitivity
        user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()

        # if user enters an invalid choice, prompt user to choose a valid choice
        if user_choice not in choices:
            print("Invalid choice. Please enter 'rock', 'paper', or 'scissors'.")
            continue
        # Add delay for a more interactive experience
        time.sleep(1.2)
        # Get the computer's choice using the random.choice() method
        computer_choice = random.choice(choices)

        # Display both user and computer choices each round
        print("You chose:", user_choice)
        print("Computer chose:", computer_choice)

        # Determine the winner for each round
        # If the user and computer choices are the same, it's a tie
        if user_choice == computer_choice:
            print("It's a tie!")
            # Increment the ties variable by 1
            ties += 1
        # If user chooses rock and computer chooses scissors, user wins the round
        elif user_choice == "rock" and computer_choice == "scissors":
            print("You win!")
            # Increment user score variable by 1
            user_score += 1
        # If user chooses paper and computer chooses rock, user wins the round
        elif user_choice == "paper" and computer_choice == "rock":
            print("You win!")
            # Increment user score variable by 1
            user_score += 1
        # If user chooses scissors and computer chooses paper, user wins the round
        elif user_choice == "scissors" and computer_choice == "paper":
            print("You win!")
            # Increment user score variable by 1
            user_score += 1
        # If none of the above conditions are met, computer wins the round
        else:
            print("Computer wins!")
            # Increment computer score by 1
            cpu_score += 1

        # update the score for each round
        if user_score < 2 and cpu_score < 2:
            print("Current score:")
            print("Your score:", user_score, '| ' + "Computer score:", cpu_score)
            print(' '*5, "Ties:", ties, '| ' + "Round:", rounds_played)
            # Add a delay before the next round for a more interactive experience
            print('Next round in 1.5 seconds...')
            time.sleep(1.5)
    # Add a delay before the final results are displayed for a more interactive experience
    time.sleep(2.5)
    # Print the final score
    print("\nGame over! Here is the final results:")
    print("Your score:", user_score, '| ' + "Computer's score:", cpu_score)
    print(' '*5, "Ties:", ties, '| ' + "Rounds played:", rounds_played)

    # Ask the user if they want to play again
    play_again = input("Would you like to play again? (yes or no): ").lower()
    if play_again == "no":
        # use break to end the while loop and exit the game
        break

# Goodbye message
time.sleep(2)
print("\nThanks for playing a game of Rock, Paper, Scissors!")
print('To follow my programming progress please visit my GitHub\nby clicking on the following link: ')
print('www.github.com/trudrewski')