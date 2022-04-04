a= int(input(''))
count = 0
b=a
while True:
    count +=1
    old = (b//10)+(b%10)
    b = (b%10)*10 + (old%10)

    if a == b:
        break

print(count)