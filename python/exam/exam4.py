def fac(x):
    res=1
    for i in range(1, x+1):
        res *=i
    return res
def PER(n,r):
    return fac(n)/fac(n-r)

print("n's value:")
n=int(input(''))
print("n's value:")
r=int(input(''))

print(int(PER(n,r)))