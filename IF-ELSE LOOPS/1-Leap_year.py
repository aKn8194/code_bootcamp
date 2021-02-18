# Python program to check leap year
# A year which is divisible by 400, or, a year divisible by 4 but not divisible 100, is a leap year.

#----------------------------------------------------
#NAVIE METHOD
# Reading year from user 
year = int(input('Enter year: '))

# Checking for loop and taking decision
if (year%400==0) or (year%4==0 and year%100!=0):
    print('LEAP YEAR')
else:
    print('NOT LEAP YEAR')
#----------------------------------------------------
# CALENDAR LIBRARY
# importing calendar library
import calendar

# Reading year from user 
year = int(input('Enter year: '))

# Calling isleap() method on calendar library
isLeap = calendar.isleap(year)

# Taking decision
if isLeap = True:
    print('LEAP YEAR')
else:
    print('NOT LEAP YEAR')