print("I'm trying to learn on a daily basis")
import sys
print(sys.version)

##Syntax
#Try this without indentation and it will give a syntax error.
if 5 > 2:
  print("Five is greater than two!")

#This works too
if 5 > 2:
 print("Five is greater than two!") 
if 5 > 2:
        print("Five is greater than two!") 
#You have to use the same number of spaces in the same block of code, otherwise Python will give you an error:
"""
if 5 > 2:
 print("Five is greater than two!")
        print("Five is greater than two!")
"""
        
## Variables

x = 5
y = "Ferdinand and Bellingham"
print(x)
print(y)


#Variables do not need to be declared with any particular type, and can even change type after they have been set.

x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)