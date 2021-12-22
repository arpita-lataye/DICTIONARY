a={'1': 'Austin Little', '2': 'Natasha Howard', '3': 'Alfred Mullins', '4': 'Jamie Rowe'}
m=[]
for i in a:
    # print(a[i])
    m.append(i)
    m.append(a[i])
# print(m)
# [1, red,2,green , 3, black, 4 ,white, 5, black]
n=[]
g=[]
count=0
for i in range(len(m)):
    if count==2:
        n.append(g)
        g=[]
        count=1
    else:
        count+=1
    g.append(m[i])
n.append(g)
print(n)