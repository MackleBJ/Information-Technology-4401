# Brett M.
# INFOTC 4401-01
# Challenge: Improved Object Position Calculation

while True:
    try:
        initial_position = float(input("Enter the initial position (meters): "))
    except:
        initial_position = float(input("Oops! Please enter a number for initial position (meters): "))
    try:
        initial_velocity = float(input("Enter the initial velocity (meters/second): "))
    except:
        initial_velocity = float(input("Oops! Please enter a number for the initial velocity (meters/second): "))
    try:
        acceleration = float(input("Enter the acceleration (meters/second^2): "))
    except:
        acceleration = float(input("Oops! Please enter a number for the acceleration (meters/second^2): "))

    try:
        time = float(input("Enter the time elapsed (seconds): "))
        while True:
            if time < 0:
                time = float(input("Oops! Please enter a number greater than or equal to 0 for the time elapsed (seconds): "))
            else:
                break
    except:
        time = float(input("Oops! Please enter a number greater than or equal to 0 for the time elapsed (seconds): "))
        while True:
            if time < 0:
                time = float(input("Oops! Please enter a number greater than or equal to 0 for the time elapsed (seconds): "))
            else:
                break

    final_position = initial_position + (initial_velocity * time) + ((1/2) * acceleration * time**2)
    print("\nInitial position = {} meters".format(initial_position))
    print("Initial velocity = {} meters/second".format(initial_velocity))
    print("Acceleration = {} meters/second^2".format(acceleration))
    print("Time elapsed = {} seconds\n".format(time))

    print("The object's final position is {} meters.".format(final_position))

    while True:
        answer = input("Would you like to perform another calculation? (y/n) ")
        if answer.strip() == "y":
            break
        elif answer.strip() =="n":
            exit()
        else:
            continue
