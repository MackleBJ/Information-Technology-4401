# Brett M.
# INFOTC 4401-01
# Challenge: Random Number File Writer

import random

# Function to get limits
def retrieve_number (title):
    while True:
        try:
            number = int(input("Please enter a positive non-zero number for {} ".format(title)))
            if number <= 0:
                print("Oops! Please enter a positive non-zero number. ")
                continue
            else:
                break
        except:
            print("Oops! That's an invalid entry. ")
            continue
    return number

# Function to produce random numbers (total, lower limit, upper limit)
list_of_numbers = []
def create_random_numbers (total, lower_limit, upper_limit):
    counter = 0
    while counter <= total:
        list_of_numbers.append(random.randrange(lower_limit,upper_limit))
        counter += 1

# Function to write random numbers to file
def write_to_file (file_name):
    numb_file = open(file_name,"w")
    for numb in list_of_numbers:
        numb_file.write(str(numb))
        numb_file.write("\n")
    numb_file.close()
    print("{} random numbers written to {}".format((len(list_of_numbers)) - 1,file_name))
total_numbs = retrieve_number("total number(s)")
lower_limit = retrieve_number("lowest value")
upper_limit = retrieve_number("highest value")
create_random_numbers(total_numbs, lower_limit, upper_limit)
write_to_file("randomnum.txt")
