z={'V': [1, 4, 6, 10], 'VI': [1, 4, 12], 'VII': [1, 3, 8]}
# z={'V': [1, 3, 5], 'VI': [1, 5], 'VII': [2, 7, 9]}
m={}
for i in z:
    b=[]
    for j in z[i]:
        if j%2==0:
            b.append(j)
            m.update({i:b})
print(m)



z1={'V': [1, 3, 5], 'VI': [1, 5], 'VII': [2, 7, 9]}
m={}
for i in z1:
    b=[]
    for j in z1[i]:
        if j%2==0:
            b.append(j)
            m.update({i:b})
print(m)