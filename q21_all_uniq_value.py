# write a python program to print all uniqe values in a dictionary.

# a=[{'v':'S001'},{'v':'S002'},{'vi':'S001'},{'vi':'S005'},{'vii':'S005'},{'v':'S009'},{'viii':'S007'}]
# c=[]
# m={}
# for i in range (len(a)):
#     for j in (a[i]):
#         if a[i][j] not in c:
#             # c.append(a[i][j])
#             m.update({j:a[i][j]})
# print(m)

Sample=[{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"},
{"V":"S009"},{"VIII":"S007"}]
b=[]
for i in range(len(Sample)):
    for j,m in Sample[i].items() :
        if m not in b:
            b.append(m)
print(b)