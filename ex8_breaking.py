# Author: Kevin Johnson
# Created: DEC 18 2021

formatter = "{} {} {} {}"

# what happens when we...
#print(formatter.format(1, 2, 3)) 
# IndexError: Replacement index 3 out of range for positional args tuple

#print(formatter.format(1, 2, 3, 4, 5))
# no error, but the extra args are ignored

#print("{}".format())
# IndexError

#print("{}".format({}))
#print("{}".format("{}"))
# these work the same

blah = "xxxxx"
print("Show me value:", blah)
print(f"Show me value formatted: {blah}")
print("Show me value using format: {}".format(blah))
print("Just for giggles: {}".format("{}".format(blah)))
# these work the same