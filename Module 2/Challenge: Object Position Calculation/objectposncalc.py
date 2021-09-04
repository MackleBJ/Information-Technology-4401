# Brett M.
# INFOTC 4401-01
# Challenge: Object Position Calculation
# Purpose: Calculate an object's final position when given the initial position, initial velocity, acceleration, and time elapsed.


initial_position = float(input("Enter the initial position (meters): "))
initial_velocity = float(input("Enter the initial velocity (meters/second): "))
acceleration = float(input("Enter the acceleration (meters/second^2): "))
time = float(input("Enter the time elapsed (seconds): "))

final_position = initial_position + (initial_velocity * time) + ((1/2) * acceleration * time**2)
print("\nInitial position = {} meters".format(initial_position))
print("Initial velocity = {} meters/second".format(initial_velocity))
print("Acceleration = {} meters/second^2".format(acceleration))
print("Time elapsed = {} seconds\n".format(time))

print("The object's final position is {} meters.".format(final_position))
