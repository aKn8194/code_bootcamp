# Finding area and volume of sphere
# Area = 4πr2
# Volume =(4/3)πr3

# importing math module for PI
import math

# Reading temperature in Celsius
radius = float(input('Enter radius of circle: '))

# Calculating area and volume
area = 4 * math.pi * radius ** 2
volume = (4/3) * math.pi * radius**3

# Displaying output
print('Area = %0.4f.' % (area))
print('Volume = %0.4f.' % (volume))