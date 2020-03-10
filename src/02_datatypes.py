"""
Python is a strongly-typed language under the hood, which means
that the types of values matter, especially when we're trying
to perform operations on them.

Note that if you try running the following code without making any
changes, you'll get a TypeError saying you can't perform an operation
on a string and an integer.
"""

x = 5
y = "7"

# Write a print statement that combines x + y into the integer value 12

## Understand 
# Need to mathmatically add the values of x and y

## Plan
# I will write a simple print statement that adds x and y

## Execute
# print(x+y) didn't work
print(x+int(y)) # this does!

## Reflect
# Unsupported operand type for +: 'int' and 'str'
# This means one of my variables is a string (it's y)
# I need a method to convert a str into an int


# Write a print statement that combines x + y into the string value 57

## Understand
# I need to print a statement that combines x and y into a string of 57

## Plan
# I will use the same methods as above, but for combination, not addition
# I will need a method to convert an int to a string

## Execute
print(str(x)+y) # This works!

## Reflect
# Is there another way to do this?
