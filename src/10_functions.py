# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE
def is_even(num):
    if int(num) % 2 == 0:
        return "true"
    else:
        return "false"
# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)
print(is_even(num))
# Print out "Even!" if the number is even. Otherwise print "Odd"

# YOUR CODE HERE
def is_even_odd(num):
    if int(num) % 2 == 0:
        return f"{num} is even"
    else:
        return f"{num} is odd"

print(is_even_odd(num))
