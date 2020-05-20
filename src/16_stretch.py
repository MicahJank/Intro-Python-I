# 3. Write a program to determine if a number, given on the command line, is prime.

#    1. How can you optimize this program?
#    2. Implement [The Sieve of
#       Eratosthenes](https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes), one
#       of the oldest algorithms known (ca. 200 BC).


import sys
import math

# in order to check if a number is prime i need to find if it has any factors besides 1 and itself - if it does it is not a prime number
# i only need to check the numbers up to the square root of the number being inputted
# i should start my loop at 2 since 1 is not relevant

# First i will need to get the number that the user is inputting into the command line
    # sys.args will give me everything that has been inputted on the command line

# I will then need to find the square root of that number - this number will be the last number i need to check in the loop

# I will need to loop starting at 2 all the way until i get to the square root of the number the user inputted

# inside the loop i need to check if the current index in the loop is divisible by the number the user inputted - if it is - then that means the number is not prime

# if i get to the end of the loop and none of the index numbers have been divisible by the number then there is a good chance it is a prime


inputs = sys.argv
number = 0
isPrime = False

def run_program(num):
    num = int(num)
    print("Running")
    
    sqrt = int(math.sqrt(num))
    
    for factor in range(2, sqrt):
        if num % factor == 0:
            return False
    
    return True


try:
    number = inputs[1]
except:
    print("No number inputted - please make sure you are inputting a number into the command line")
else:
    print(f"Number inputted: {number}")
    isPrime = run_program(number)
    print(f"{number} is a prime number" if isPrime == True else f"{number} is not a prime number") 




