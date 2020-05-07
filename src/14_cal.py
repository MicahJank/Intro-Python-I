"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py [month] [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.

Note: the user should provide argument input (in the initial call to run the file) and not 
prompted input. Also, the brackets around year are to denote that the argument is
optional, as this is a common convention in documentation.

This would mean that from the command line you would call `python3 14_cal.py 4 2015` to 
print out a calendar for April in 2015, but if you omit either the year or both values, 
it should use today’s date to get the month and year.
"""

import sys
import calendar
from datetime import datetime

# Things i dont know
# - How do i get values from the command line? - I need to be able to do this in order to grab the month and day the user inputs when running the start command
  # print(sys.argv) will print me the command line input with everything put inside a list for me all i would need to do is remove the first item from the list and then i would be left with
  # a list that just hast he 2 arguments i want - the month and year
  # 
# - How do i print a calendar using the calendar and/or datetime module i imported?
  # print(datetime.today().month) - gives me the current month
  # print(datetime.today().year) - gives me the current year
  # print(calendar.month(2020, 5)) - prints out the calendar with the specified year and month


# First i need to get the arguments from the command line

# Next i need to use the calendar module to print out the calendar with that month and year the user specified

# if the user doesnt put in a month or year - i need to use the datetime module to find the systems current month and year and use those values instead when printing the calendar

# if the user passes only 1 argument - i need to assume that is the month and print the calendar using that month and the systems current year

inputs = sys.argv

def check_month_input(monthNum):
    # there is a chance a user will put in a letter for the month instead of a number - in this case the casting will throw an error
    # so it is better that i catch it here then have the program error out
    try:
        monthNum = int(monthNum)
    except:
        print("Invalid string type for month input - please make sure your month input is a number between 1 and 12")
        return
    else: 
        if monthNum < 1 or monthNum > 12:
            print("Invalid month input - please make sure your month input is a number between 1 and 12")

if len(inputs) == 1:
    month = datetime.today().month
    year = datetime.today().year
    print(calendar.month(year, month))
elif len(inputs) == 2:
    check_month_input(inputs[1])
    month = inputs[1]
    year = datetime.today().year
    print(calendar.month(year, month))
