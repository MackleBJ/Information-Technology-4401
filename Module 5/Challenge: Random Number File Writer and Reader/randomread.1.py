# Brett M.
# INFOTC 4401-01
# Challenge: Random Number File Reader

list_of_numbers = []

# Function to read and count numbs from file.
def read_file():
    numb_file = open("randomnum.txt", "r")

    for rand_numb in numb_file:
        list_of_numbers.append(rand_numb[slice(0,len(rand_numb)-1)])

    numb_file.close()
    return list_of_numbers

# Function to display numbers and final count.
def display_numbs():
    print("The random numbers in randomnum.txt are: ")

    for number in list_of_numbers:
        print(number)

    print("\nThe total random number count is {}".format(len(list_of_numbers)))

read_file()
display_numbs()
