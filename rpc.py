from os import system
from random import randint

system('clear')

# Variable Declarations
weapons = {1:"rock", 2:"paper", 3:"scissors"}
greeting = "Welcome to the Rock Paper Scissors Challenge."
computer_guess = randint(1,3)

def the_game():
    '''this is where we play'''
    print("+" * (len(greeting) + 2))
    print(greeting)
    print("+" * (len(greeting) + 2))
    # Menue of options availabe
    for key,value in weapons.items():
        print("{} to play {}.".format(key,value.capitalize()))
    # User makes their choice
    user_play = int(input("Choose Your Weapon: "))
    if user_play not in [1,2,3]:
        print("Not a valid option, chose again")
        the_game()

the_game()

if computer_guess == 1:
    print("Computer Played {}".format(weapons[computer_guess]))

if computer_guess == 2:
    print("Computer Played {}".format(weapons[computer_guess]))

if computer_guess == 3:
    print("Computer Played {}".format(weapons[computer_guess]))
