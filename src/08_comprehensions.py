"""
List comprehensions are one cool and unique feature of Python.
They essentially act as a terse and concise way of initializing
and populating a list given some expression that specifies how
the list should be populated. 

Take a look at https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
for more info regarding list comprehensions.
"""

# Write a list comprehension to produce the array [1, 2, 3, 4, 5]
## Understand
# I need to insert an array using a list comprehension
## Plan
# I can use range
# I can use a for loop as well
## Execute
y = [i for i in range(1, 6)]

print (y)

# Write a list comprehension to produce the cubes of the numbers 0-9:
# [0, 1, 8, 27, 64, 125, 216, 343, 512, 729]

## Plan (Understanding is similar to Problem 1)
# I need to insert 0-9 using the same methods as above
# Using operators, I need to cube each value
## Execute
y = [i**3 for i in range(10)]

print(y)

# Write a list comprehension to produce the uppercase version of all the
# elements in array a. Hint: "foo".upper() is "FOO".
## Plan
# I need to take the values of list a and put them into list y
# We have access to the upper method

a = ["foo", "bar", "baz"]

y = [i.upper() for i in a]

print(y)

# Use a list comprehension to create a list containing only the _even_ elements
# the user entered into list x.

x = input("Enter comma-separated numbers: ").split(',')

# What do you need between the square brackets to make it work?

## Reflect
# TypeError: not all arguments converted during string formatting
# This means that i is currently a string and you cant do math on a string
y = [int(i) for i in x if int(i) % 2 == 0]

print(y)