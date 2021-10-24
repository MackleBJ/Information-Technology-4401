# Brett M.
# INFOTC 4401-01
# Challenge: Recursion and Python Turle Graphics

import turtle
import random

def turtle_migration_recursion(direction, mileage, decrement):
    turtle.bgcolor("#12fce9")
    turtle.pensize(1)
    turtle.pencolor("white")
    turtle.forward(mileage)
    turtle.left(direction)
    mileage -= decrement
    direction = direction - 60
    if mileage > 0:
        turtle_migration_recursion(direction,mileage, 0.25)

def main():
    SWIM_SPEED = 0
    turtle.speed(SWIM_SPEED)
    direction = 360/random.randrange(1,360)
    nautical_miles = 200
    turtle_migration_recursion(direction,nautical_miles, 0.25)

main()
