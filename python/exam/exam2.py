x= input(" ")
print("숫자:",x)
x_list= list(map(int, str(x)))
print("결과: ")
for i in range(len(x)):
    print(i+1,":", x[i])