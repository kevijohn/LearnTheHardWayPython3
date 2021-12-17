# Author: Kevin Johnson
# Created: DEC 16 2021

print("Mary had a little lamb.")
print("Its fleece was white as {}.".format('snow'))
print("And everywhere that Mary went.")
print("." * 10) # what'd that do?  It printed the string 10 times
end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"
# watch end = ' ' at the end. try removing it to see what happens
#
# Looks like end= overrides the last character of the print statement.
# Assuming the print function appends the python-specific carriage return new line character
# to everything it prints.
print(end1 + end2 + end3 + end4 + end5 + end6, end=' ')
print(end7 + end8 + end9 + end10 + end11 + end12)

# Extra
print("Is 'end' some kind of key word?", end='\t\t\t')
print("Should be same line")