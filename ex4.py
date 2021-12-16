# Author: Kevin Johnson
# Created: DEC 16 2021

cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")

# Study drills
# 1. If space_in_a_car is written as 4 instead of 4.0, then carpool_capacity
# is printed as an ingeter instead of a floating point number.

# Using python as a calculator now with variable names:
#
#PS C:\Users\...\LearnTheHardWayPython3> python     
#Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
#Type "help", "copyright", "credits" or "license" for more information.
#>>> blah = 3
#>>> blah 
#3
#>>> blah * blah
#9
#>>> quit()