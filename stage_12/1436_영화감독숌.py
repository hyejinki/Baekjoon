N = int(input())
count = 1
dic = {}
num = 665         # while문 안에 바로 1 더해줄 거라서 665부터 시작
while count <= N:   # 구하는 N번째 까지만
    num += 1
    if '666' in str(num):     # '666'찾아
        count += 1
            
print(num)        # N번째의 num