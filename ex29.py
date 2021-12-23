# Author: Kevin Johnson
# Created: DEC 23 2021

people = 20
cats = 30
dogs = 15

if people < cats:
    print("Too many cats! The world is doomed!")

if people > cats:
    print("Not many cats!  The world is saved!")

if people < dogs:
    print("The world is drooled on!")

if people > dogs:
    print("The world is dry!")

dogs += 5

if people >= dogs:
    print("People are greater than or equal to dogs.")

if people <= dogs:
    print("People are less than or equal to dogs.")

if people == dogs:
    print("People are dogs.")

# Study drills
# 1. The if will run the code under it if the logical condition is met
# 2. The code under the if needs to be intended so Python knows which lines should be executed
# 3. If the code isn't indented, then it won't be controlled by the logical condition next to the if