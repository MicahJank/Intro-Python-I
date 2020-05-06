"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"

# YOUR CODE HERE
with open("./src/foo.txt", "r") as foo:
    read_data = foo.read()
    print(read_data)

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain
with open('./src/bar.txt', 'w') as bar:
    bar.write("I have a pen, I have an apple - uh - apple pen!")
    bar.write("I have a pen, I have pineapple - uh - pineapple pen!")
    bar.write("Apple pen...Pineapple pen.... - uh - Pen pineapple apple pen!")

# YOUR CODE HERE