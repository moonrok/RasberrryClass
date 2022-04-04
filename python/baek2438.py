i= int(input(" "))
j=0
k=0
for j in range(i):
    k=j
    for k in range(j+1):
        print("*", end='')
    j+=1
    print('')
