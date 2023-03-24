import cmath
a=float(input('Enter the coefficient of x**2: '))
b=float(input('Enter the coefficient of x: '))
c=float(input('Enter the constant coefficient: '))

discriminant=(b*2-4*a*c)
root1= -b + cmath .sqrt(discriminant)
root2= -b - cmath .sqrt(discriminant)

if discriminant==0:
    print(f'Has one roots: root= {-b/2*a}')
elif discriminant > 0:
    print(f'Has two roots:')
    print(f'Root 1: {root1}')
    print(f'Root 2: {root2}')
else:
    print(f'Has no real roots!')

