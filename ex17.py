# Author: Kevin Johnson
# Created: DEC 19 2021

from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}")

# We could do these two on one line, how?
in_file = open(from_file)
inData = in_file.read()

print(f"The input file is {len(inData)} bytes long")

print(f"Does the output file exist? {exists(to_file)}")
print(f"Ready, hit RETURN to continue, CTRL-C to abort.")
input()

out_file = open(to_file, 'w')
out_file.write(inData)

print("Alright, all done.")

out_file.close()
in_file.close()
