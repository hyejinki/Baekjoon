users = [[40, 10000], [25, 10000]]
emoticons = [7000, 9000]
# print(len(users))
sale = [10, 20, 30, 40]
sale.sort(reverse=True)
for s in sale:
    for i in range(len(users)):
        if users[i][0] == s:
            # while ans 
            # for c in emoticons:
                # if c * ((100 - s) * 0.01)