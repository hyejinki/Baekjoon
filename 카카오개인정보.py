today = "2022.05.19"
terms = ["A 6", "B 12", "C 3"]
privacies = ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]

p = len(privacies)
t = len(terms)
date = []
term = []

today = today.split('.')
for x in privacies:
    date.append(x.replace(' ', '.').split('.')) 

print(date)
for x in terms:
    term.append(x.split(' '))
for i in range(p):
    for j in range(t):
        if date[i][-1] == term[j][0]:
            div = (int(term[j][1]) + int(date[i][1])) // 12
            mod = (int(term[j][1]) + int(date[i][1])) % 12
            if mod == 0:
                mod = 1

            year = int(date[i][0]) + div
            month = mod
            if int(today[0]) > year \
                or int(today[0]) == year and int(today[1]) > month\
                or (int(today[0]) == year and int(today[1]) == month\
                and int(today[2]) >= int(date[i][2])):
                answer.append(i+1)
            break
