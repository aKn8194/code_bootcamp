# Celsius to Fahrenheit & Kelvin

# Fahrenheit = 1.8 * Celsius + 32
# Kelvin = 273.15 + Celsius

# Reading temperature in Celsius
celsius = float(input('Enter temperature in celsius: '))

#Converting
fahrenheit = 1.8 * celsius + 32
kelvin = 273.15 + celsius

#Show results
print('%.3f Celsius = %.3f Fahrenheit.'%(celsius,fahrenheit))
print('%.3f Celsius = %.3f Kelvin.'%(celsius,kelvin))