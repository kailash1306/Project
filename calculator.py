def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
a=int(input("enter first number :"))
b=int(input("enter second number :"))
op = int(input("enter Operation to be done :\n1)Add\n2)Subtract\n3)Multiply\n4)Divide\n: "))
if(op==1):
    print(add(a,b))
elif(op==2):
    print(sub(a,b))
elif(op==3):
    print(mul(a,b))
elif(op==4):
    print(div(a,b))
else:
    print("Invalid output")