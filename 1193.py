# 1/1 | 1/2 2/1 | 3/1 2/2 1/3 -> 분자 분모 따로 보면 하나씩 증가 or 감소

x = int(input())
k = i = 1
while(x > k):       #몇 번째 줄인지 확인 i
    k = 1 + k + i
    i += 1

mol = (k - x + 1)   #분자(홀수 기)
den = (i - (k - x))    #분모

if (i % 2 == 0):
    print(str(den)+ '/' + str(mol))
else:
    print(str(mol)+ '/' + str(den))