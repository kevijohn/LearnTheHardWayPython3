# Author: Kevin Johnson
# Created: DEC 15 2021

# Study drill comments: this statement just prints a string
print("I will now count my chickens:")

# print string then print result of math calculation in-line with prev string
# print("Hens", 25 + 30 / 6) # original line from the book
print("Hens", 25.0 + 30.0 / 6.0) # trying to use floating point numbers
print("Roosters", 100 - 25 * 3 % 4.0)

# print a string
print("Now I will count the eggs:")

# print just result of math calculation without preceeding string
print(3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6.0)

# show that a math operation enclosed in quotes is just a string
print("is it true that 3 + 2 < 5 - 7?")

# show that when math operation is not enclosed, then a result is calculated
print(3 + 2 < 5 - 7)

# reinforce that math in quotes is just a string, math outside quotes gets calculated
print("What is 3 + 2?", 3 + 2)
print("What is 5 - 7?", 5 - 7)

# print strings
print("Oh, that's why it's False.")

print("How about some more.")

# print boolean result of comparison operation
print("Is it greater?", 5 > -2)
print("Is it greater or equal?", 5 >= -2)
print("Is it less or equal?", 5 <= -2)

# Using python from the terminal as a calculator:
#
#PS C:\Users\...\LearnTheHardWayPython3> python     
#Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
#Type "help", "copyright", "credits" or "license" for more information.
#>>> 2 + 2
#4
#>>> quit()