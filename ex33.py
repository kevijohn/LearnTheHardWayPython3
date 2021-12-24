# Author: Kevin Johnson
# Created: DEC 24 2021

# NOTE: this file has been modified from the original script from the book
# according to the Study Drills for the exercise.

from sys import argv

script, iterations_str, interval_str = argv

numbers = []

def the_loop(times, interval):
    i = 0
    while i < times:
        print(f"At the top i is {i}")
        numbers.append(i)

        i += interval
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")

# run the loop
the_loop(int(iterations_str), int(interval_str))

print("The numbers: ", end=" ")

for num in numbers:
    print(num, end=" ")