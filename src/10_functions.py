# Write a function is_even that will return true if the passed-in number is even.

def if_even_true(num):
    if num % 2 == 0:
        return True
    else:
        return False

# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"

def print_number(num):
    if num % 2 == 0:
        return "Even!"
    else:
        return "Odd.."

print(print_number(num))
print(if_even_true(num))