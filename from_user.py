a={}
n=int(input('number of elements:'))
for i in range(n):
    k=input('enter key:')
    v=input('enter value:')
    a.update({k:v})
print(a)