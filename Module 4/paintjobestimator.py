 Brett M.
# INFOTC 4401-01
# Challenge: Paint Job Estimator

import math

while True:
    # Ask user for the square footage.
    try:
        square_footage = float(input("Please enter the square footage of wall space: "))
    except:
        while True:
            try:
                square_footage = float(input("Please enter a numerical value for square footage: "))
                break
            except:
                continue
    # Ask the user for the price per gallon of paint.
    try:
        price_per_gallon = float(input("Please enter the price per gallon of paint: "))
    except:
        while True:
            try:
                price_per_gallon = float(input("Please enter a numerical value for price per gallon: "))
                break
            except:
                continue

    # Perform calculations to find all variables of concern.
    gallons_of_paint = math.ceil(square_footage / 350)
    hours_of_work = gallons_of_paint * 6
    cost_of_paint = price_per_gallon * gallons_of_paint
    cost_of_labor = gallons_of_paint * 62.25
    total_cost = cost_of_labor + cost_of_paint

    # Print out all information calculated.
    print("The number of gallons of paint required {}".format(int(gallons_of_paint)))
    print("The hours of labor required {0:.1f}".format(float(hours_of_work)))
    print("The cost of the paint ${0:.2f}".format(cost_of_paint))
    print("The labor charges ${0:.2f}".format(cost_of_labor))
    print("The total cost of the paint job ${0:.2f}".format(total_cost))

    # Request if the user would like to perform another calculation.
    response = input("Would you like to do another estimate? (y/n) ")
    if response == "y":
        continue
    else:
        exit()
