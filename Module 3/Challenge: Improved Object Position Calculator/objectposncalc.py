# Brett McElvain (Student Number: 16071946)
# INFOTC 4401-01
# Challenge: Improved Object Position Calculation

while True:
    # Ask user for initial position (with exception handling).
    try:
        initial_position = float(input("Enter the initial position (meters): "))
    except:
        while True:
            try:
                initial_position = float(input("Oops! Please only enter a numerical value for initial position (meters): "))
                break
            except:
                continue

    # Ask user for initial velocity (with exception handling).
    try:
        initial_velocity = float(input("Enter the initial velocity (meters/second): "))
    except:
        while True:
            try:
                initial_velocity = float(input("Oops! Please only enter a numerical value for initial velocity (meters/second): "))
                break
            except:
                continue

    # Ask user for acceleration (with exception handling).
    try:
        acceleration = float(input("Enter the acceleration (meters/second^2): "))
    except:
        while True:
            try:
                acceleration = float(input("Oops! Please only enter a numerical value for acceleration (meters/second^2): "))
                break
            except:
                continue

    # Ask user for time (with exception handling).
    try:
        time = float(input("Enter the time elapsed (seconds): "))
    except:
        while True:
            try:
                time = float(input("Oops! Please only enter a numerical value greater than or equal to 0 for time elapsed (seconds): "))
                if time < 0:
                    continue
                else:
                    break
            except:
                continue

    # Perform calculation to find final position.
    final_position = initial_position + (initial_velocity * time) + ((1/2) * acceleration * time**2)

    # Print out the information entered.
    print("\nInitial position = {} meters".format(initial_position))
    print("Initial velocity = {} meters/second".format(initial_velocity))
    print("Acceleration = {} meters/second^2".format(acceleration))
    print("Time elapsed = {} seconds\n".format(time))

    # Print out the final position.
    print("The object's final position is {} meters.".format(final_position))

    # Check to see if user would like to perform another calculation.
    while True:
        answer = input("Would you like to perform another calculation? (Enter: yes or no) ")
        if answer.strip() == "yes":
            break
        elif answer.strip() == "no":
            exit()
        else:
            continue
