a=[
     {"first":"1"}, 
     {"second": "2"}, 
     {"third": "1"}, 
     {"four": "5"}, 
     {"five":"5"}, 
     {"six":"9"},
     {"seven":"7"}
]
c=[]
for i in range (len(a)):
    for j in (a[i]):
        if a[i][j] not in c:
            c.append(a[i][j])
print(c)
print(len(a))