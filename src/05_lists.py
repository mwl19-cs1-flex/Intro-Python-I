# For the exercise, look up the methods and functions that are available for use
# with Python lists.

x = [1, 2, 3]
y = [8, 9, 10]

# For the following, DO NOT USE AN ASSIGNMENT (=).

# Change x so that it is [1, 2, 3, 4]
## Understand
# I need to append 4 to the end of the list
## Plan 
# What method can I use to append something to a list?
# I can use the append() method
## Execute
x.append(4)
print(x)

# Using y, change x so that it is [1, 2, 3, 4, 8, 9, 10]
## Understand
# I need to append the end of list X with the contents of Y
## Plan
# What method can I use to put a list in a list?
# I can use the extend() method
x.extend(y)
print(x)

# Change x so that it is [1, 2, 3, 4, 9, 10]
## Understnad
# I need to remove 8 from the list of x
## Plan
# I can use the remove() method
x.remove(8)
print(x)

# Change x so that it is [1, 2, 3, 4, 9, 99, 10]
## Understand
# I need to add 99 to the second from the last place on the list
# -1 is the last item in the list, so -2 would be the second to last item
## Plan
# I can use the insert() method, with the postion being -2
## Execute
# x.insert(-2, 99) not correct
x.insert(-1, 99) # correct
## Reflect
# -2 was one two many positions
print(x)

# Print the length of list x
## Understand
# I need to print the length of x
## Plan
# I can use len()
## Execute
print(len(x))

# Print all the values in x multiplied by 1000
## Understand
# For each item in list x I need to multiply it by 1000
## Plan
# I can use a for loop and insert the value into y, a new empty list
## Execute
y = []
for i in x:
    y.append(i*1000)
print(y)