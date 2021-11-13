'''write a python program to sort (ascending and descending) a dictionary by value.'''

import operator
d={1:2,3:4,4:3,2:1,0:0}
print('original dictionaly:',d)
sorted_d=sorted(d.items(),key=operator.itemgetter(1))
print('dictionary in ascending order by value:',sorted_d)

sorted_d=dict(sorted(d.items(),key=operator.itemgetter(1),reverse=True))
print('dictionary in descending order by value:',sorted_d)


a={1:2,3:4,4:3,2:1,0:0}
max=0
b={}
for i in a:
    if a[i]>max:
        max=a[i]
        s=i
# print(max)
a.pop(s)
b.update({s:max})
smax=0
for i in a:
    if a[i]>smax:
        smax=a[i]
        d=i
# print(smax)
a.pop(d)
b.update({d:smax})
tmax=0
for i in a:
    if a[i]>tmax:
        tmax=a[i]
        k=i
# print(tmax)
a.pop(k)
b.update({k:tmax})
fmax=0
for i in a:
    if a[i]>fmax:
        fmax=a[i]
        l=i
# print(fmax)
a.pop(l)
b.update({l:fmax})

# hmax=0
# for i in a:
#     if a[i]>hmax:
#         hmax=a[i]
#         g=i
# a.pop(g)
# b.update({g:hmax})
# print(b)
