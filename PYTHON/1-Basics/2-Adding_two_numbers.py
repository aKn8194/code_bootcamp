# Python program to find
# sum of two numbers

# Reading two numbers
number1 = input("Enter first number: ")
number2 = input("Enter second number: ")

# Converting to float
# Conversion is required because
# input() function return string

number1 = float(number1)
number2 = float(number2)

#Addition operator
result = number1 + number2

#Show results
print(f"Sum of {number1} and {number2} is {result}")