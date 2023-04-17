
privacies = ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]
p = len(privacies)
date = []
for x in privacies:
    print(x)
    date.append(x.replace(' ', '.').split('.'))
    

print(date)