# Finding largest of two numbers

# Reading numbers
first = float(input('Enter first number: '))
second = float(input('Enter second number: '))

# Making decision and displaying
if first > second:
    largest = first
else:
    largest = second
print('Largest = %d' %(largest))