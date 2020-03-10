"""
In this exercise, you'll be playing around with the sys module,
which allows you to access many system specific variables and
methods, and the os module, which gives you access to lower-
level operating system functionality.
"""

import sys
# See docs for the sys module: https://docs.python.org/3.7/library/sys.html

# Print out the command line arguments in sys.argv, one per line:

## Understand
# Print each arg in sys.argv
## Plan
# Research possible methods
# There is a fileinput method that iterates over lines
## Execute
#  import fileinput
# for line in fileinput.input():
#     print(line)
# ^ This didn't work. Process took too long.
for i in sys.argv:
    print(i)
## Reflect
# What is fileinput? 
# What other ways could I print argv?

# Print out the OS platform you're using:

## Understand
# I need to print out what OS platform I am using
## Plan 
# I can use sys.platform 
## Execute
print(sys.platform)

# Print out the version of Python you're using:

## Understand
# I need to print out the version of Python I am using:
## Plan
# I can use sys.version
## Execute
print(sys.version) 

import os
# See the docs for the OS module: https://docs.python.org/3.7/library/os.html

# Print the current process ID
## Understand
# A process is an instance of a computer program being executed
## Plan
# I can use the getpid() method
## Execute
print(os.getpid())
## Reflect
# This value changes!
# I need to invoke it!

# Print the current working directory (cwd):
## Understand
# The current working directory is where the script is being executed
## Plan 
# I can use getcwd()
## Execute
print(os.getcwd())
## Reflect
# This does not change

# Print out your machine's login name
## Understand
# The machine's login name is the name of the user logged in to the machine
## Plan
# I can use the getlogin() method
## Execute
print(os.getlogin())
## Reflect
# There is a best practice to use
import getpass
print(getpass.getuser())
# ^ This is preferred over getlogin
