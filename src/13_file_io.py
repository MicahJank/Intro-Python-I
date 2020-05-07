"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"

# YOUR CODE HERE
# note that the path in the () for open starts in whatever directory you are currently in
# since i am in the /Intro-Python-I directory that means that in order to get to the foo.txt file i need
# to go into the src folder first, if my current directory was in the src folder then i wouldnt need to go through the /src folder
# i could go straight to the foo.txt - micah
with open("./src/foo.txt", "r") as foo:
    read_data = foo.read()
    print("read_data: \n", read_data)

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain
with open('./src/bar.txt', 'w') as bar:
    bar.write("I have a pen, I have an apple - uh - apple pen! \n")
    bar.write("I have a pen, I have pineapple - uh - pineapple pen! \n")
    bar.write("Apple pen...Pineapple pen.... - uh - Pen pineapple apple pen! \n")

with open("./src/bar.txt", "r") as bar:
    bar_data = bar.read()
    print("bar_data: \n", bar_data)

# YOUR CODE HERE