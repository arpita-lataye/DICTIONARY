sub={'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}
a={}
# g=[]
for i,j in sub.items():
    # print(j)
    for k in range(len(j)):
        # print(j[k])
        a.update({i:j[k]})
        print(a)