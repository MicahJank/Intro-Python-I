# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE
def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False

# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"

# YOUR CODE HERE
# Ternary style
print("Even!" if is_even(num) == True else "Odd") 
    

num = input("Enter a number: ")
num = int(num)

# normal style
if is_even(num):
    print("Even!")
else:
    print("Odd")

 