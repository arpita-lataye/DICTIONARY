a=[[1, 'Jean Castro', 'V'], [2, 'Lula Powell', 'V'], [3, 'Brian Howell', 'VI'], [4, 'Lynne Foster', 'VI'], [5,
'Zachary Simon', 'VII']]
s={}
for i in range(len(a)):
    # print(a[i])
    # for j in a[i]:
        # print(j)
        s.update({a[i][0]:a[i][1:]})
print(s)