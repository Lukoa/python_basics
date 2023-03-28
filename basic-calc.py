def add(num1, num2):
    result=num1+num2
    return result

def sub(num1, num2):
    result=num1-num2
    return result

def div(num1, num2):
    result=num1/num2
    return result

def mult(num1, num2):
    result=num1*num2
    return result
def mod(num1, num2):
    result=num1+num2
    return result
def exp(num1,num2):
    result=num1**num2
    return result

num1=float(input("Enter the first number: "))
num2=float(input("Enter the second number: "))
op=input("Enter operator: ")

if op=="+":
    print(f"Sum is {add(num1,num2)}")
elif op=="-":
    print(f"Difference is {sub(num1,num2)}")
elif op=="/":
    print("The quotient is "+str(div(num1,num2))+".") #why use formatted string by NJOGU
elif op=="*":
    print("The product is {}".format(mult(num1,num2))) 
    """
    another formatted string
    """
elif op=="%":
    print(f"The modulus is {mod(num1,num2)}.")
elif op=="^":
    print(f"The exponential product is {exp(num1,num2)}")
else :
    print("Invalid operation!!!")