"""
Python provides a number of ways to perform printing. Research
how to print using the printf operator, the `format` string 
method, and by using f-strings.
"""

x = 10
y = 2.24552
z = "I like turtles!"

# Using the printf operator (%), print the following feeding in the values of x,
# y, and z:
# x is 10, y is 2.25, z is "I like turtles!"
## Understand
# printf is where you print values in a string
# d is for integers
# f is for floats
# s is for strings
# format is: "String %datatype" % (data to insert)
print("X is %2d y is %.2f and z is %2s" % (x, y, z))

# Use the 'format' string method to print the same thing
## Understand 
# Format method takes a string and replaces values (found by {}) with function parameters
## Plan
# I need to find a way to set y to two decimals
## Execute
print("X is {} y is {:.2f} and z is {}".format(x, y, z))

# Finally, print the same thing using an f-string
## Understand
# F-strings are simple implementations of interpolated strings
## Plan
# How do I keep it to 2 decimals?
## Execute
print(f'x is {x} y is {y:.2f} and z is {z}')