# Brett McElvain
# INFOTC 4401-01
# Student number: 16071946
# Challenge: Animal Class

from Animals import Animal

Animals = []

# Function to greet user with info about the program.
def greeting():
    print("Welcome to the animal generator!\nThis program creats Animal objects.")

# Function to ask for type, name, and then pass that to Animal.
def create_animal():
        type = input("\nWhat type of animal would you like to create? ")
        name = input("What is the animal's name? ")
        Animals.append(Animal(type, name))

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
    create_animal()
    if ask_run_again() == False:
        break
    else:
        continue
print_animal_list()
