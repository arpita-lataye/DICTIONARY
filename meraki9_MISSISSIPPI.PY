a="MISSISSIPPI"
b={}
for i in a:
    if i not in b:
        b[i]=1
    else:
        b[i]=b[i]+1
print(b)