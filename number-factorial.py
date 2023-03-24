k=int(input('Enter a positive integer: '))

factorial=1
for i in range(1, k+1):
    factorial*=i

print(f'The factorial of {k} is: {factorial}')