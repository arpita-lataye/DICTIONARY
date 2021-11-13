''' write a python script to generate and print a dictionary that contains a number(between 1 and n)
in th form (x,x*x) '''


n=int(input('enter number:'))
# d={}                         both d={} and d=dict() are use as a empty dictionary.
d=dict()
for x in range(1,n+1):
    d[x]=x*x
print(d)