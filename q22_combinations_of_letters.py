'''write a python program to create and display all combinations of letters, selecting each letter from a differentrew key in a dictionary.'''

# a={'1':['a','b'],'2':['c','d']}
# for key in (a):
#     for j in (a[key]):
#         print(key*a[1][j])

q={'b':['a','b'],'c':['d','e']}
l=[]
for i,j in q.items():
    # print(j)
    # l=[]
    for k in range(len(j)):
        l.append(j[k][0])
print(l)
for i in range(len(l)-2):
    print(l[i],l[2])   
    print(l[i],l[3])