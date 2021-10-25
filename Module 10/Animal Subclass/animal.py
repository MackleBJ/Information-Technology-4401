# Brett M.
# INFOTC 4401-01
# Challenge: Animal Subclass

import random

# Class to create animal.
class Animal:

    # Method to assign initial values.
    def __init__(self, type, name):
        self.__name = name
        self.__animal_type = type
        self.__mood = random.randrange(1,4)

    # Method to return animal type.
    def get_animal_type(self):
        return self.__animal_type

    # Method to return name.
    def get_name(self):
        return self.__name

    # Method to interpret the random number into a mood and return mood.
    def check_mood(self):
        if self.__mood == 1:
            self.__mood = "happy"
        elif self.__mood == 2:
            self.__mood = "hungry"
        else:
            self.__mood = "sleepy"
        return self.__mood

# Child class of the Animal Class to create a mammal.
class Mammal(Animal):

    # Method to assign and inherit initial values.
    def __init__(self, type, name, hair_color):
        super().__init__(type, name)
        self.__hair_color = hair_color

    # Method to return hair color.
    def get_hair_color(self):
        return self.__hair_color

# Child class of the Animal Class to create a bird.
class Bird(Animal):

    # Function to assign and inherit initial values.
    def __init__(self, type, name, can_fly):
        super().__init__(type, name)
        self.__can_fly = can_fly

    def get_can_fly(self):
        return self.__can_fly

