'''
a=int(input('Enter the first integer: '))
b=int(input('Enter the second integer: '))

#This program calculates the GCD of the two numbers
while b!=0:
    a, b =b, a % b

print(f'The GCD {a} and {b} is: {a}')
'''
'''
Using Euclidean method
'''
def gcd(a,b):
    
    if b==0:
        return a
    else:
        return gcd(b, a % b)

def lcm(a,b):
    return abs(a*b)//gcd(a,b)

a=int(input('Enter the first number: '))
b=int(input('Enter the second number: '))

print(f'The GCD of {a} and {b} is {gcd(a,b)}')
print(f'And their their LCM is: {lcm(a,b)}')
