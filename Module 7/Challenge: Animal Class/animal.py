# Brett McElvain
# INFOTC 4401-01
# Student number: 16071946
# Challenge: Animal Class

import random

# Class to create animal.
class Animal:

    # Function to assign initial values.
    def __init__(self, type, name):
        self.__name = name
        self.__animal_type = type
        self.__mood = random.randrange(1,3)

    # Function to return animal type.
    def get_animal_type(self):
        return self.__animal_type

    # Function to return name.
    def get_name(self):
        return self.__name

    # Function to interpret the random number into a mood and return mood.
    def check_mood(self):
        if self.__mood == 1:
            self.__mood = "happy"
        elif self.__mood == 2:
            self.__mood = "hungry"
        else:
            self.__mood = "sleepy"
        return self.__mood
