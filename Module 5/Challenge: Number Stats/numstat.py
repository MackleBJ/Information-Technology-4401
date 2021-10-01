# Brett M.
# INFOTC 4401-01
# Challenge: Number Stats

list_of_numbs = []
# Function to open specified file and collect numbers.
def open_file(file_name):
    numb_file = open(file_name,"r")
    for numb in numb_file:
        list_of_numbs.append(int(numb))
    print("File name: {}".format(file_name))

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

open_file("numbers.txt")
get_sum()
get_count()
calc_average()
get_max()
get_min()
calc_range()
