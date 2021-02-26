# Python program to find
# multiply of two numbers

# Reading two numbers
number1 = input("Enter first number: ")
number2 = input("Enter second number: ")

# Converting to float
# Conversion is required because
# input() function return string

number1 = float(number1)
number2 = float(number2)

#Addition operator
result = number1 * number2

#Show results
print("%0.2f * %0.2f = %0.2f" %(number1,number2, result))