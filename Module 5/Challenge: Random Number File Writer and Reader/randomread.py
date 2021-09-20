# Brett M.
# INFOTC 4401-01
# Challenge: Random Number File Reader

# Read random numbs. from "randomnum.txt".
numb_file = open("randomnum.txt", "r")

# Count / Display numbs. read from file.
counter = 0
list_of_numbers = []

for rand_numb in numb_file:
    list_of_numbers.append(rand_numb[slice(0,len(rand_numb)-1)])
    counter += 1

numb_file.close()

# Display final numb. count.
print("The random numbers in randomnum.txt are: ")

for number in list_of_numbers:
    print(number)

print("\nThe total random number count is {}".format(counter))
