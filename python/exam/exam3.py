def ADD(x,y):
    return x+y
def Subtract(x,y):
    return x-y
def Multiply(x,y):
    return x*y
def Division(x,y):
    return x/y
print("x,y Input Data:")
x, y= map(int,input().split())
A=ADD(x,y)
S=Subtract(x,y)
M=Multiply(x,y)
D=Division(x,y)
print('Select :')
cal= input('')
if cal=='A' or cal=='a':
    ADD(x,y)
    print(x,'+',y,'=',A)
if cal=='S' or cal=='s':
    Subtract(x,y)
    print(S)
if cal=='M' or cal=='m':
    Multiply(x,y)
    print(M)
if cal=='D' or cal=='d':
    Division(x,y)
    print(D)