# dict1={'c1':'red','c2':'green','c3':None}
# print('original dictionary:',dict1)

# dict1={key:value for (key,value)in dict1.items()if value is not None}
# print(dict1)


a={'c1': 'Red', 'c2': 'Green', 'c3': None}
print('original dictionary:',a)
b={}
for i,j in a.items():
    # print(j)
    if j!=None:
        b.update({i:j})
print(b)