# Brett M.
# INFOTC 4401-01
# Challenge: Animal Class

from Animals import Animal
from Animals import Mammal
from Animals import Bird


Animals = []

# Function to greet user with info about the program.
def greeting():
    print("Welcome to the animal generator!\nThis program creats Animal objects.")

# Funciton to ask user if they'd like to create a mammal or a bird.
def mammal_or_bird():
    print("\nWould you like to create a mammal or bird?")
    print("1. Mammal\n2. Bird")
    answer = input("Which would you like to create? ")
    if answer == "1":
        return "Mammal"
    else:
        return "Bird"

# Function to ask for type, name, and then pass that to Animal.
def create_animal(mammal_or_bird):
    type = input("\nWhat type of {} would you like to create? ".format(mammal_or_bird))
    name = input("What is the {}'s name? ".format(mammal_or_bird))
    if mammal_or_bird == "Mammal":
        hair_color = input("What color is the mammal's hair? ")
        Animals.append(Mammal(type, name, hair_color))
    else:
        can_fly = input("Can the bird fly? ")
        Animals.append(Bird(type, name, can_fly))

# Function to ask user if they'd like to create another animal.
def ask_run_again():
    answer = input("\nWould you like to add more animals (y/n)? ")
    if answer == "y":
        return True
    else:
        return False

# Function to print all animals the user created.
def print_animal_list():
    position = 0
    print("\nAnimal List: ")
    while position < len(Animals):
        print("{} the {} is {}".format(Animals[position].get_name(), Animals[position].get_animal_type(), Animals[position].check_mood()))
        position += 1
    exit()

greeting()
while True:
    answer_to_mammal_or_bird = mammal_or_bird()
    create_animal(answer_to_mammal_or_bird)
    if ask_run_again() == False:
        break
    else:
        continue
print_animal_list()
