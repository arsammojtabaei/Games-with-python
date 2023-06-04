import random

def get_user_choice():
    choice = input("Enter your choice (rock/paper/scissors): ").lower()
    while choice not in ['rock', 'paper', 'scissors']:
        print("Invalid choice. Please try again.")
        choice = input("Enter your choice (rock/paper/scissors): ").lower()
    return choice

def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif user_choice == 'rock':
        if computer_choice == 'paper':
            return "Computer wins!"
        else:
            return "You win!"
    elif user_choice == 'paper':
        if computer_choice == 'scissors':
            return "Computer wins!"
        else:
            return "You win!"
    elif user_choice == 'scissors':
        if computer_choice == 'rock':
            return "Computer wins!"
        else:
            return "You win!"

def play_again():
    choice = input("Do you want to play again? (yes/no): ").lower()
    while choice not in ['yes', 'no']:
        print("Invalid choice. Please try again.")
        choice = input("Do you want to play again? (yes/no): ").lower()
    return choice == 'yes'

def play_game():
    print("Welcome to Rock, Paper, Scissors!")
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print("You chose:", user_choice)
        print("Computer chose:", computer_choice)
        print(determine_winner(user_choice, computer_choice))
        if not play_again():
            break

play_game()
