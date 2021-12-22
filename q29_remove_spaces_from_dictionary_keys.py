Original= {'S 001': ['Math', 'Science'], 'S  002': ['Math','English']}
# print(Original)
a={}
for i,p in Original.items():
    # print(i)
    for j in i:
        # print(j)
        if j is ' ':
            k=i.replace(" ", "")
            a.update({k:p})
print(a)