# Author: Kevin Johnson
# Created: DEC 24 2021

the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# Sorry Zed, I'm not transcribing your comments

for number in the_count:
    print(f"This is count {number}")

for fruit in fruits:
    print(f"A fruit of type: {fruit}")

for i in change:
    print(f"I got {i}")

#elements = []
#
#for i in range(0, 6):
#    print(f"Adding {i} to the list.")
#    elements.append(i)

#for i in elements:
#    print(f"Element was: {i}")
rangeElem = range(0,6)  # This works as well, no loop needed

for i in rangeElem:
    print(f"rangeElem was {i}")