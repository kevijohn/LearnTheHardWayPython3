# Author: Kevin Johnson
# Created: DEC 16 2021
import math

name = 'Kevin Johnson'
age = 43 # unfortunately not a lie
height = 68 # inches
weight = 190 # lbs
eyes = 'Hazel'
teeth = 'White' # wtf
hair = 'Sandy Brown'

print(f"Let's talk about {name}.")
print(f"He's {height} inches tall.")
print(f"He's {weight} pounds heavy.")
print("Actually that's too heavy, he could stand to lose a few pounds.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")

# Study drills
height_whole_feet = math.floor(height / 12)
height_remainder = height % 12
height_in_cm = height * 2.54
print(f"My height is {height} inches, which is also {height_whole_feet} feet and {height_remainder} inches and {height_in_cm} centimeters.")
