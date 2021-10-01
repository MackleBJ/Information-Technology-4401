# Brett M.
# INFOTC 4401-01
# Challenge: Number Stats

import math

list_of_numbs = []

# Function to open specified file and collect numbers.
def open_file(file_name):
    numb_file = open(file_name,"r")
    for numb in numb_file:
        list_of_numbs.append(int(numb))

# Function to get sum.
def get_sum():
    print("Sum: {}".format(sum(list_of_numbs)))

# Function to count the total amount of numbers.
def get_count():
    print("Count: {}".format(len(list_of_numbs)))

# Function to calculate average of all numbers (sum - count).
def calc_average():
    print("Average: {}".format((sum(list_of_numbs))/(len(list_of_numbs))))

# Function to find the max number value.
def get_max():
    print("Maximum: {}".format(max(list_of_numbs)))

# Function to find the min. number value.
def get_min():
    print("Minimum: {}".format(min(list_of_numbs)))

# Function to find the range of the numbers (max - min.).
def calc_range():
    print("Range: {}".format((max(list_of_numbs))-(min(list_of_numbs))))

# Function to find the median of the numbers.
def get_median():
    if (len(list_of_numbs)%2) == 0:
        list_of_numbs.sort()
        position = int(len(list_of_numbs)/2)
        high_position = list_of_numbs[position]
        low_position = list_of_numbs[position - 1]
        median_number = (high_position + low_position)/2
        print("Median: {}".format(median_number))

    elif (len(list_of_numbs)) == 1:
        print("Median: {}".format(list_of_numbs[0]))

    else:
        list_of_numbs.sort()
        median_number = list_of_numbs[math.floor((len(list_of_numbs))/2)]
        print("Median: {}".format(median_number))

# Function to find the mode of the numbers.
def get_mode():
    number_of_each_number = {}
    for number in list_of_numbs:
        if number in number_of_each_number:
            number_of_each_number[number] += 1
        else:
            number_of_each_number[number] = 1

    max_count = 0
    mode_number = []
    for number in number_of_each_number:
        count_value = number_of_each_number[number]
        if count_value > max_count:
            max_count = count_value
    for number in number_of_each_number:
        count_value = number_of_each_number[number]
        if count_value == max_count:
            mode_number.append(number)
    print("Mode: {}".format(mode_number))

# Function to request if user would like to try another file.
def ask_if_run_again():
    answer = input("Would you like to evaluate another file? (y/n) ")
    return answer

while True:
    file_name = input("Please enter the file name: ")
    open_file(file_name)

    if len(list_of_numbs) == 0:
        print("There are no numbers in {}".format(file_name))
        answer = ask_if_run_again()
        list_of_numbs = 0
        if answer == "y":
            continue
        else:
            exit()
    else:
        get_sum()
        get_count()
        calc_average()
        get_max()
        get_min()
        calc_range()
        get_median()
        get_mode()
        answer = ask_if_run_again()
        list_of_numbs = []
        if answer == "y":
            continue
        else:
            exit()
