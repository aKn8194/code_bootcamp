# Simple and Compound Interest
# Simple Interest = (P*T*R)/100
# Compound Interest = P * ( (1+r/100 )t - 1)

# Reading principal amount, rate and time
principal = float(input('Enter principal amount: '))
rate = float(input('Enter rate: '))
time = float(input('Enter time: '))

#Calculation 
simple_interest = (principal*time*rate)/100
compound_interest = principal * ( (1+rate/100)**time - 1)

#Show results
print('Simple interest is: %0.3f'%(simple_interest))
print('Compound interest is: %0.3f'%(compound_interest))