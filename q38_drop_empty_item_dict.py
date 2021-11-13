dict1={'c1':'red','c2':'green','c3':None}
print('original dictionary:',dict1)

dict1={key:value for (key,value)in dict1.items()if value is not None}
print(dict1)


for (key,value) in dict1.items():
    if value is  not None:
        print(dict1)