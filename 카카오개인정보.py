
privacies = ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"]
terms = ["Z 3", "D 5"]
today = "2020.01.01"
p = len(privacies)
t = len(terms)
date = []
term = []
ans = []
today = today.split('.')
for x in privacies:
    date.append(x.replace(' ', '.').split('.')) 
for x in terms:
    term.append(x.split(' '))
for i in range(p):
    for j in range(t):
        if date[i][-1] == term[j][0]:
            div = (int(term[j][1]) + int(date[i][1])) // 12
            mod = (int(term[j][1]) + int(date[i][1])) % 12
            year = int(date[i][0]) + div
            month = mod
            if int(today[0]) > year \
                or int(today[0]) == year and int(today[1]) > month\
                or (int(today[0]) == year and int(today[1]) == month\
                and int(today[2]) >= int(date[i][2])):
                ans.append(i+1)
            break
            
print(ans)
# print(date)