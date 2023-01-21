# 소인수분해

num = int(input())
lis_num= []
num2 = num

while(num2 != 1):
    for i in range(2, num+1):
        if num2 % i == 0:
            num2 = num2 / i 
            lis_num.append(i)
            break

for i in lis_num:
    print(i)