numbers = [273, 103, 5, 32, 65, 72, 800, 99]
even_sum = 0
odd_sum = 0

for x in numbers:
    if x % 2 ==0:
        even_sum = even_sum + x
    elif x% 2 ==1 :
        odd_sum = odd_sum + x
print('짝수의 합:',even_sum)
print('홀수의 합:',odd_sum)