# Brett M.
# INFOTC 4401-01
# Challenge: Random Number File Writer

import random

# Request how many random numbers to generate (positive & non-zero numb.).
while True:
    try:
        total_to_generate = int(input("Please enter a positive non-zero integer for total number(s) you want: "))
        if total_to_generate <= 0:
            continue
        else:
            break
    except:
        continue
        
# Request lower limit of number range (positive & non-zero numb.).
while True:
    try:
        lower_limit = int(input("Please enter a positive non-zero integer for lowest value number(s) you want: "))
        if lower_limit <= 0:
            continue
        else:
            break
    except:
        continue

# Request upper limit of number range (positive & non-zero numb.).
while True:
    try:
        upper_limit = int(input("Please enter a positive non-zero integer for highest value number(s) you want: "))
        if upper_limit <= 0:
            continue
        else:
            break
    except:
        continue

# Write random numbers to "randomnum.txt" with all numbs. on sep. lines.
counter = 1
numb_file = open("randomnum.txt", "w")

while counter <= total_to_generate:
    numb_file.write(str(random.randrange(lower_limit, upper_limit)))
    numb_file.write("\n")
    counter += 1

numb_file.close()

# Print notification of what file numbs. written to.
print("{} random number(s) written to randomnum.txt".format(total_to_generate))
