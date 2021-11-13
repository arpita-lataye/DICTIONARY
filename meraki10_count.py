dic =  {
   'Alex': ['subj1', 'subj2', 'subj3'], 
   'David': ['subj1', 'subj2']}
count=0
# for i in range(len(dic)):
#     for j in (dic[i]):
#         if a[i] is list:
#             count=count+dic[i][j]
# print(count)

for x in dic:
    for y in range(len(dic[x])):
        count=count+1
print(count)