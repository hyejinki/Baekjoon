<<<<<<< HEAD

privacies = ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"]
terms = ["Z 3", "D 5"]
today = "2020.01.01"
=======
today = "2022.05.19"
terms = ["A 6", "B 12", "C 3"]
privacies = ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]

>>>>>>> 646e7556a1a25f20e9a4b77c2a7d45c01335f956
p = len(privacies)
t = len(terms)
date = []
term = []
<<<<<<< HEAD
ans = []
today = today.split('.')
for x in privacies:
    date.append(x.replace(' ', '.').split('.')) 
=======

today = today.split('.')
for x in privacies:
    date.append(x.replace(' ', '.').split('.')) 

print(date)
>>>>>>> 646e7556a1a25f20e9a4b77c2a7d45c01335f956
for x in terms:
    term.append(x.split(' '))
for i in range(p):
    for j in range(t):
        if date[i][-1] == term[j][0]:
            div = (int(term[j][1]) + int(date[i][1])) // 12
            mod = (int(term[j][1]) + int(date[i][1])) % 12
<<<<<<< HEAD
=======
            if mod == 0:
                mod = 1

>>>>>>> 646e7556a1a25f20e9a4b77c2a7d45c01335f956
            year = int(date[i][0]) + div
            month = mod
            if int(today[0]) > year \
                or int(today[0]) == year and int(today[1]) > month\
                or (int(today[0]) == year and int(today[1]) == month\
                and int(today[2]) >= int(date[i][2])):
<<<<<<< HEAD
                ans.append(i+1)
            break
            
print(ans)
# print(date)
=======
                answer.append(i+1)
            break
>>>>>>> 646e7556a1a25f20e9a4b77c2a7d45c01335f956
