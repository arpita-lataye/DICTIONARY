# write a python program to print all uniqe values in a dictionary.

a=[{'v':'S001'},{'v':'S002'},{'vi':'S001'},{'vi':'S005'},{'vii':'S005'},{'v':'S009'},{'viii':'S007'}]
c=[]
for i in range (len(a)):
    for j in (a[i]):
        if a[i][j] not in c:
            c.append(a[i][j])
print(c)