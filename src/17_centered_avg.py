# Return the "centered" average of an array of ints, 
# which we'll say is the mean average of the values, 
# except ignoring the largest and smallest values in the array. 
​
# centered_average([1, 2, 3, 4, 100]) 3
# centered_average([1, 1, 5, 5, 10, 8, 7])  5
# centered_average([-10, -4, -2, -4, -2, 0])  -3
​
# Understand
# "mean average": 2, 3, 4 --> 3
# are arrays sorted?  NO
#  are all values different, or are some duplicate? Some are duplicate
# assumption: we will always 3 or more values
# No mutating the list
# maybe non-integers
​
# Plan:
# how to get largest and smallest?
​
    # find and remove the min and max
    # sort the array
​
def centered_average(a_list):
    # make a copy
    copy_list = a_list.copy()
    # sort the list
    copy_list.sort()
    # slice the list to exclude the first and last elements
    list_to_sum = copy_list[1:-1]
    # sum the list
    return sum(list_to_sum)/len(list_to_sum)
​
## Plan the second
# find the min
# find the max
# sum the list
# subtract min and max
​
print(centered_average([1, 2, 3, 4, 100]))
​
# Reflect
# duplicate list --> space complexity
# MOAR tests