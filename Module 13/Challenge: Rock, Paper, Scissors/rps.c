# Brett M.
# INFOTC 4401-01
# Challenge: Rock, Paper, Scissors
# Purpose: Create the game Rock, Paper, Scissors.

import random
import pickle
import logging

# Function to display the first Main Menu.
def main_menu():
    print("1. Start New Game")
    print("2. Load Game")
    print("3. Quit")
    answer = input("\nEnter choice: ")

    return answer

# Function to display the second Main Menu.
def main_menu_two():
    print("\nWhat would you like to do?\n")
    print("1. Play Again")
    print("2. View Statistics")
    print("3. Quit")
    answer = input("\nEnter choice: ")

    return answer

# Function to create and gather the new game's info.
def start_new_game():
    name = input("\nWhat is your name? ")
    print("\nHello {}. Let's Play!".format(name))
    game_stats = {'Name':name, 'Wins':0, 'Losses': 0, 'Ties':0, 'Rounds':1}

    return name, game_stats

# Function to load a game's info.
def load_game():
    name = input("\nWhat is your name? ")
    try:
        file_name = name + ".rps"
        game_file = open(file_name, "rb")
        game_stats = pickle.load(game_file)
        game_file.close()
        print("\nWelcome back {}. Let's play!".format(name))

        return name, game_stats

    except:
        game_stats = {'Name':name, 'Wins':0, 'Losses': 0, 'Ties':0, 'Rounds':1}
        print("\n{}, your game could not be found.".format(name))

        return name, game_stats

# Function to save the game's info.
def save_game(name):
    try:
        file_name = name + ".rps"
        game_file = open(file_name, "wb")
        pickle.dump(game_stats, game_file, pickle.HIGHEST_PROTOCOL)
        game_file.close()
        print("\n{}, your game has been saved.".format(name))
    except Exception as exception:
        print("\nSorry {}, the game could not be saved.".format(name))
        logger = logging.getLogger('ftpuploader')
        logger.error(str(exception))

# Function to create the random computer's choice.
def computer_choice():
    choice2 = random.randint(1,3)
    if choice2 == 1:
        choice2 = 'Rock'
    elif choice2 == 2:
        choice2 = 'Paper'
    elif choice2 == 3:
        choice2 = 'Scissors'

    return choice2

# Fucntion to determine the winner of the game.
def find_winner(choice1, choice2):
    if choice1 == choice2:
        winner = 'Tie'
    elif choice1 == 'Rock' and choice2 == 'Paper':
        winner = 'Computer'
    elif choice1 == 'Rock' and choice2 == 'Scissors':
        winner = 'Player'
    elif choice1 == 'Paper' and choice2 == 'Rock':
        winner = 'Player'
    elif choice1 == 'Paper' and choice2 == 'Scissors':
        winner = 'Computer'
    elif choice1 == 'Scissors' and choice2 == 'Rock':
        winner = 'Computer'
    elif choice1 == 'Scissors' and choice2 == 'Paper':
        winner = 'Player'

    return winner

# Function to display game menu and round text.
def game(game_stats):
    print("\nRound {}\n".format(game_stats['Rounds']))
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")

    while True:
        choice = input("\nWhat will it be? ")
        if choice == '1':
            choice = 'Rock'
            break
        elif choice == '2':
            choice = 'Paper'
            break
        elif choice == '3':
            choice = 'Scissors'
            break
        else:
            print('Please enter the number 1, 2, or 3.')
            continue

    comp_choice = computer_choice()

    winner = find_winner(choice, comp_choice)
    if winner == 'Computer':
        game_result = 'lose'
        game_stats['Losses'] += 1
        game_stats['Rounds'] += 1
    elif winner == 'Player':
        game_result = 'win'
        game_stats['Wins'] += 1
        game_stats['Rounds'] += 1
    else:
        game_result = 'tie'
        game_stats['Ties'] += 1
        game_stats['Rounds'] += 1

    print("\nYou chose {}. The computer chose {}. You {}!".format(choice, comp_choice, game_result))

print("Welcome to Rock, Paper, Scissors!")
while True:
    answer = main_menu()
    # Start new game.
    if answer == '1':
        name, game_stats = start_new_game()
        game(game_stats)
    # Load game.
    elif answer == '2':
        name, game_stats = load_game()
        game(game_stats)
    # Quit.
    elif answer == '3':
        print("\nSorry that you didn't have time to play. Have a great day!")
        exit()
    # Invalid entry.
    else:
        print("Please enter the number 1, 2, or 3.\n")
        continue

    while True:
        answer = main_menu_two()
        # Play again.
        if answer == '1':
            game(game_stats)
        # View Statistics.
        elif answer == '2':
            print("\n{}, here are your game play statistics...".format(name))
            print("Wins: {}".format(game_stats['Wins']))
            print("Losses: {}".format(game_stats['Losses']))
            print("Ties: {}".format(game_stats['Ties']))
            if game_stats['Losses'] == 0:
                print("\nWin/Loss Ratio: {:.2f}".format(float(game_stats['Wins'])))
            else:
                print("\nWin/Loss Ratio: {:.2f}".format((game_stats['Wins'])/(game_stats['Losses'])))
        # Quit.
        elif answer == '3':
            save_game(name)
            exit()
        # Invalid entry.
        else:
            print("Please enter the number 1, 2, or 3.\n")

