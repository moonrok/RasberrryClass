a=int(input(''))
b=int(a%4)
c=int(a%100)
d=int(a%400)

if b==0 and c!=0:
    print('1')
elif d==0:
    print('1')
else:
    print('0')