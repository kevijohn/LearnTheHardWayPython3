# Author: Kevin Johnson
# Created: DEC 18 2021

# import module to access command line arguments
from sys import argv

# take the filename that was passed in
script, filename = argv

# open the filename, assign returned object to a variable in the script
txt = open(filename)

# print the filename that was passed in
print(f"Here's your file {filename}:")
# read the contents of the file and print it on the terminal
print(txt.read())
txt.close()

## prompt the user for the filename
#print("Type the filename again:")
#file_again = input("> ")
#
## open the filename, assign returned object to a different variable
#text_again = open(file_again)
#
## read the contents of the file and print it on the terminal
#print(text_again.read())
#text_again.close()