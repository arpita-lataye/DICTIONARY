dict1 = {'Alex': ['subj1', 'subj2', 'subj3'], 'David': ['subj1', 'subj2']}
count=0
for i,j in dict1.items():
    # print(j)
    for k in j:
        count+=1
print('total count of value:',count)